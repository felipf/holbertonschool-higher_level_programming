$(document).ready(function () {
  // AJAX GET request to the URL
  $.get("https://swapi-api.hbtn.io/api/people/5/?format=json", function (data) {
    const characterName = data.name;
    $("#character").text(characterName);
  });
});
