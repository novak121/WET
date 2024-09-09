let answer = Math.floor(Math.random() * 20) + 1;
let no_of_guesses = 0;
let guesses_num = [];
function guessing() {
    let user_guess = document.getElementById("zkus").value;
    if (user_guess < 1 || user_guess > 20) {
        alert("Toto číslo není v dosahu, zkuste znovu!");
    } else {
        guesses_num.push(user_guess);
        no_of_guesses += 1;
        if (user_guess < answer) {
            outcome1.textContent = "Moc nízké";
            outcome2.textContent = "Počet pokusů : " + no_of_guesses;
            outcome3.textContent = "Číslo bylo: " + guesses_num;
        } else if (user_guess > answer) {
            outcome1.textContent = "Moc velké";
            outcome2.textContent = "Ne, už nemáš pokusy : " + no_of_guesses;
            outcome3.textContent = "Číslo bylo: " + guesses_num;
        } else if (user_guess == answer) {
            outcome1.textContent = "Správně!!";
            outcome2.textContent = "Číslo bylo.. " + answer;
            outcome3.textContent =
                " pokus Č. " + no_of_guesses + "Celkem pokusů";
        }
    }
}
let outcome1 = document.getElementById("outcome1");
let outcome2 = document.getElementById("outcome2");
let outcome3 = document.getElementById("outcome3");
