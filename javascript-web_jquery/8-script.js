$(document).ready(function () {
  // AJAX GET request to the URL
  $.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
    data.results.forEach(function (movie) {
      const title = movie.title;
      $("<li>").text(title).appendTo("#list_movies");
    });
  });
});
