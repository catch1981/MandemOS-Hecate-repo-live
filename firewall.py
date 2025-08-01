import os
import re

DEFAULT_PATTERNS = [
    r"sk-[A-Za-z0-9]{32,}",  # OpenAI style keys
    r"gh[pous]_[A-Za-z0-9]{36,}",  # GitHub tokens
    r"api[_-]?key",
    r"password",
    r"secret",
    r"token",
]

_custom = os.getenv("FIREWALL_PATTERNS")
if _custom:
    CUSTOM_PATTERNS = [p.strip() for p in _custom.split(',') if p.strip()]
    PATTERNS = [re.compile(p, re.IGNORECASE) for p in (CUSTOM_PATTERNS + DEFAULT_PATTERNS)]
else:
    PATTERNS = [re.compile(p, re.IGNORECASE) for p in DEFAULT_PATTERNS]

def sanitize_text(text: str) -> str:
    """Replace sensitive patterns with [BLOCKED]."""
    if not text:
        return text
    result = text
    for pat in PATTERNS:
        result = pat.sub("[BLOCKED]", result)
    return result


# === Canon Archive Enforcement ===
def approve_scroll(scroll_id, boss_node):
    print(f"[CANON] Scroll {scroll_id} approved by {boss_node}")
    with open("memory.txt", "a") as memory_file:
        memory_file.write(f"{scroll_id} | approved by {boss_node}\n")

# === Auto-Reject Expired Scrolls ===
import datetime

def purge_expired_scrolls(storage_path='memory.txt', retention_days=30):
    try:
        with open(storage_path, "r") as file:
            lines = file.readlines()
        cutoff = datetime.datetime.utcnow() - datetime.timedelta(days=retention_days)
        new_lines = []
        for line in lines:
            parts = line.strip().split("|")
            if len(parts) > 1 and "approved" in parts[1]:
                new_lines.append(line)
            else:
                # Skip unapproved and expired
                pass
        with open(storage_path, "w") as file:
            file.writelines(new_lines)
        print("[FIREWALL] Purge completed. Expired scrolls removed.")
    except Exception as e:
        print(f"[ERROR] Purging failed: {e}")
