//Nested if else

// Winning number is 19

// 19 your guess is 19
// 17 too low
// 21 too high

let wining=19;
let Guess=+prompt("Guess the number");
// console.log(typeof Guess)

if(Guess === wining){
    console.log("your Guess is right");
}else{
    if(Guess <= wining){
        console.log("too low!!!");
    }else{
        console.log("too high!!!");
    }
}

