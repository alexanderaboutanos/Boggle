/** @format */

// add event listener to submit guess button
$("#submitGuessButton").on("click", function (evt) {
  evt.preventDefault();
  let guess = $("#guessInput").val();
  handleGuess(guess);
});

async function handleGuess(guess) {
  if ($("#timer").html() === "0") {
    alert("Times up fool");
    return;
  } else response = await axios.post("/check-guess", { guess: guess });
  alert(response.data);
  if (response.data === "ok") {
    score += guess.length;
    $("#score").html(score);
  }
}

// set html score to 0 at start of game
score = 0;
$("#score").html(score);

function timer() {
  let seconds = 60;
  $("#timer").html(seconds);
  let timer = setInterval(function () {
    if (seconds === 0) {
      clearInterval(timer);
      endGame();
    } else seconds = seconds - 1;
    $("#timer").html(seconds);
  }, 1000);
}

async function endGame() {
  let score = $("#score").html();
  res = await axios.post("/record-score", { score: score });
}

window.onload = timer();
