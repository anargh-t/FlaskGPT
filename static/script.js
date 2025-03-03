document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("chat-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") sendMessage();
});
document.getElementById("new-chat").addEventListener("click", () => location.reload());

function sendMessage() {
    let input = document.getElementById("chat-input").value;
    let model = document.getElementById("model-select").value;

    fetch("/chat/send_message", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: input, model: model })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("chat-box").innerHTML += `<p>User: ${input}</p><p>Bot: ${data.response}</p>`;
    });
}
