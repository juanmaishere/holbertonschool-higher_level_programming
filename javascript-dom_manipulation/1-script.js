// 1-script.js
function handlecolor(){
  head.style.color = 'red';
}
// Select the header element using document.querySelector
var head = document.querySelector('header');
var click = document.querySelector('#red_header');

click.addEventListener('click', handlecolor);
