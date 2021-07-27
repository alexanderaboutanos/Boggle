/** @format */

// add event listener to submit guess button
$("#submitGuessButton").on("click", function (evt) {
  evt.preventDefault();
  let guess = $("#guessInput").val();
  handleGuess(guess);
});

async function handleGuess(guess) {
  //check to make sure the time isn't up!
  if ($("#timer").html() === "0") {
    alert("Times up fool");
    return;
  }

  // check to make sure the guess hasn't already happened!
  else if (guessedWords.includes(guess)) {
    alert("You already guessed that!");
    return;
  }

  // check if the guess is valid using the backend
  else response = await axios.post("/check-guess", { guess: guess });
  alert(response.data);

  // if the guess was valid, add it to the score and list of guessed words!
  if (response.data === "ok") {
    score += guess.length;
    $("#score").html(score);
    guessedWords.push(guess);
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
guessedWords = [];
