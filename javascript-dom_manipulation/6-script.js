function response(response) {
  if (!response.ok) {
    console.log("failed to fetch");
  } else {
    return response.json();
  }
}

function fetchName(data) {
  document.querySelector("#character").textContent = data.name;
}

function fetchError(error) {
  console.log(error);
}

const promise = fetch("https://swapi-api.hbtn.io/api/people/5/?format=json");
promise.then(response).then(fetchName).catch(fetchErrorError);
