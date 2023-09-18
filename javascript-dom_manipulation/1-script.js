let header = document.querySelector("header");
let red_header = document.querySelector("#red_header");

function colorChange() {
  header.style.color = "#FF0000";
}

red_header.addEventListener("click", colorChange);
