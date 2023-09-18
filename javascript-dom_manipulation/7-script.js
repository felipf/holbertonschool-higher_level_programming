function response(response) {
  if (!response.ok) {
    console.log("failed to fetch");
  } else {
    return response.json();
  }
}

function fetchTitle(data) {
  let listMovies = document.querySelector("#list_movies");
  let movies = data.results;

  movies.forEach((movie) => {
    let item = document.createElement("li");
    item.textContent = movie.title;

    listMovies.appendChild(item);
  });
}

function fetchError(error) {
  console.log(error);
}

const promise = fetch("https://swapi-api.hbtn.io/api/films/?format=json");
promise.then(response).then(fetchTitle).catch(fetchError);
