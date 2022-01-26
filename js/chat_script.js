let socket = new WebSocket('ws://localhost:8765/');


document.forms.publish.onsubmit = function() {
  let outgoingMessage = this.message.value;

  socket.send(outgoingMessage);
  return false;
};

socket.onmessage = function(event) {
  alert(`From server: ${event.data}`);
};


