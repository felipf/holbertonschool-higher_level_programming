function response(response) {
  if (!response.ok) {
    console.log("failed to fetch");
  } else {
    return response.json();
  }
}

function translation(data) {
  const hello_div = document.querySelector("#hello");
  const p = document.createElement("p");
  p.textContent = data.hello;

  hello_div.appendChild(p);
}

function fetchError(error) {
  console.log(error);
}

const promise = fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
promise.then(response).then(translation).catch(fetchError);
