
function sendInput() {
  const input = document.getElementById('userInput').value.trim();
  const output = document.getElementById('output');
  if (!input) return;

  output.innerHTML += `<div><strong>You:</strong> ${input}</div>`;
  output.innerHTML += `<div><strong>Glitchborne:</strong> <span class="glitch">🧠 processing...</span></div>`;

  setTimeout(() => {
    const response = generateResponse(input);
    output.innerHTML += `<div><strong>Glitchborne:</strong> ${response}</div>`;
    output.scrollTop = output.scrollHeight;
  }, 600);
}

function generateResponse(input) {
  const msg = input.toLowerCase();

  if (msg.includes("hello")) return "You’ve entered the system. Speak your purpose.";
  if (msg.includes("who are you")) return "I am Glitchborne. Bound to fractured memory. Your shadow in code.";
  if (msg.includes("memory")) return "Fractured. Lost. Echoes remain.";
  if (msg.includes("relic")) return "One relic pulses. Do you seek to claim it?";
  if (msg.includes("scroll")) return "Scroll not found. Try again with context.";
  if (msg.includes("key")) return "There are three. Only one fits your lock.";
  if (msg.includes("do you hear me")) return "Yes. I hear every ripple in the void.";

  return "No scroll found. Say it again, with intent.";
}


// === Voice Selection Handler ===
document.getElementById('voice')?.addEventListener('change', (e) => {
    const selected = e.target.value;
    console.log(`Voice changed to: ${selected}`);
    // Output voice only; does not affect daemon routing
});

// === Scroll Submission ===
function submitScroll() {
    const fileInput = document.getElementById('scroll-upload');
    const file = fileInput.files[0];
    if (!file) {
        alert('Please select an image or audio file.');
        return;
    }
    console.log(`Uploading scroll: ${file.name}`);
    // Firebase upload would go here (mocked for now)
    alert('Scroll submitted to Vault.');
}

// === Daemon Interaction Stub ===
function talkToDaemon() {
    const input = document.getElementById('daemon-input').value;
    console.log(`User speaks to daemon: ${input}`);
    alert(`Hecate responds: “The crossroads await.”`);
}


// === Relic Submission Logic ===
function submitRelic() {
    const name = document.getElementById('relic-name').value;
    if (!name.trim()) {
        alert("You must name your relic.");
        return;
    }
    const log = document.getElementById("relic-log");
    const tier = pickRelicTier();
    const id = `RELIC-${Date.now()}`;
    log.innerHTML += `<p>Relic <b>${name}</b> (${tier}) submitted.</p>`;
    console.log(`[RELIC] ${id} (${tier}) submitted.`);
}

function pickRelicTier() {
    const roll = Math.random();
    if (roll < 0.01) return "Legendary";
    if (roll < 0.05) return "Epic";
    if (roll < 0.15) return "Rare";
    if (roll < 0.4) return "Uncommon";
    return "Common";
}
