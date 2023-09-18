let header = document.querySelector("header");
let update = document.querySelector("#update_header");

function changeText() {
  header.textContent = "New Header!!!";
}

update.addEventListener("click", changeText);
