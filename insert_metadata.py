import sqlite3
import json
import os
from setup_database import DB_NAME, setup_database

METADATA_FILE = 'metadata.json'

def insert_metadata():
    if not os.path.exists(DB_NAME):
        setup_database()

    with open(METADATA_FILE, 'r') as f:
        data = json.load(f)

    name = data.get('name')
    description = data.get('description')
    if not (name and description):
        raise ValueError('metadata.json missing name or description')

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO scrolls (name, description) VALUES (?, ?)',
        (name, description)
    )
    conn.commit()
    conn.close()
    print(f"Inserted '{name}' into scrolls table of {DB_NAME}.")

if __name__ == '__main__':
    insert_metadata()


# === Relic Drop Engine ===

import random
import json
from datetime import datetime

RELIC_TIERS = {
    "Common": 0.6,
    "Uncommon": 0.25,
    "Rare": 0.1,
    "Epic": 0.04,
    "Legendary": 0.01
}

def generate_relic_metadata(name, submitted_by="Fractured"):
    tier = random.choices(list(RELIC_TIERS.keys()), weights=RELIC_TIERS.values())[0]
    relic_id = f"RELIC-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}"
    relic_data = {
        "id": relic_id,
        "name": name,
        "tier": tier,
        "effect": "Unknown until triggered",
        "status": "pending",
        "submitted_by": submitted_by,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    with open("memory.txt", "a") as f:
        f.write(json.dumps(relic_data) + "\n")

    print(f"[RELIC] {relic_id} ({tier}) submitted by {submitted_by}")
    return relic_data
