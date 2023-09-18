let header = document.querySelector("header");
let toggleHeader = document.querySelector("#toggle_header");

function colorChange() {
  header.classList.toggle("red");
  header.classList.toggle("green");
}

toggleHeader.addEventListener("click", colorChange);
