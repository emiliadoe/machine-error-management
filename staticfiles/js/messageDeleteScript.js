const message = document.querySelector('.message');
console.log(message)

if (message) {
  setTimeout(() => {
    message.style.transition = 'opacity 0.5s';
    message.style.opacity = 0;
    setTimeout(() => message.remove(), 500);
  }, 5000);
}