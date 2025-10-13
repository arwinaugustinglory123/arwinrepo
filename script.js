const chatForm = document.getElementById('chatForm');
const chatInput = document.getElementById('chatInput');
const chatMessages = document.getElementById('chatMessages');

chatForm.addEventListener('submit', function(e) {
  e.preventDefault();
  const message = chatInput.value.trim();
  if (message) {
    addMessage(message, 'user');
    chatInput.value = '';
    chatInput.focus();

    // Simulate bot reply (for demo)
    setTimeout(() => {
      addMessage('You said: ' + message, 'bot');
    }, 700);
  }
});

function addMessage(text, sender) {
  const msgDiv = document.createElement('div');
  msgDiv.className = 'message' + (sender === 'user' ? ' user' : '');
  msgDiv.textContent = text;
  chatMessages.appendChild(msgDiv);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}
