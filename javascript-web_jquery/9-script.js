$(document).ready(function () {
  // AJAX GET request to the URL
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data) {
    const translation = data.hello;
    $("#hello").text(translation);
  });
});
