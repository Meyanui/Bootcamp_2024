console.log("Hello")

let birthYear = 1990
let futureYear = 2025
let myAge = futureYear-birthYear
let myMessage = `I will be ${myAge} in ${futureYear}`

console.log(myMessage);

// utility function - instead of using console.log to print, create yours e.g
function out(...args){
  console.log(...args);
}
/////////////////////////////////////////////////////////////////////////////////

// format for creating functions:
function name() {
  return;
}

//In your enterprise you receive a bonus of 10% on your salary on ages between 26 and 32; 25% for those who are between 36 and 44. no bonus for those who are less than 26 and more than 44. represent this information in javascript//

function calculateBonus(age, salary) {
  
  if (age < 0 || salary <= 0) {
    return "wrong Information";
  }

  let bonusPercentage;

  if (age >= 26 && age <= 32) {
    bonusPercentage = 0.1; 
  } else if (age >= 36 && age <= 44) {
    bonusPercentage = 0.25; 
  } else {
    bonusPercentage = 0; 
  }






let time = 10

if (time <9 ) {
  out("Good Morning")
  else if(time < 12){
    out("Good day")
  }
}

/////////////////////////////////////////////////////////////








