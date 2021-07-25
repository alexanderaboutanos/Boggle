/** @format */

// add event listener to submit guess button
$("#submitGuessButton").on("click", function (evt) {
  evt.preventDefault();
  let guess = $("#guessInput").val();
  handleGuess(guess);
});

async function handleGuess(guess) {
  response = await axios.post("/check-guess", { guess: guess });
  alert(response.data);
  if (response.data === "ok") {
    score += guess.length;
    $("#score").html(score);
  }
}

// set html score to 0 at start of game
score = 0;
$("#score").html(score);
