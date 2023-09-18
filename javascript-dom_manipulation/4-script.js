let addLi = document.querySelector("#add_item");
let list = document.querySelector(".my_list");

function addListItem() {
  let li = document.createElement("li");
  li.textContent = "Item";
  list.appendChild(li);
}

addLi.addEventListener("click", addListItem);
