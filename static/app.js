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
}
