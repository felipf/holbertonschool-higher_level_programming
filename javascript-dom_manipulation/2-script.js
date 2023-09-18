let header = document.querySelector("header");
let red_header = document.querySelector("#red_header");

function colorChange() {
  header.classList.add("red");
}

red_header.addEventListener("click", colorChange);