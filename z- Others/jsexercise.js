/*1. Create a structured HTML file linked to a JS file
  2. Write a Javascript function that takes a parameter: myAge
  3. In the function, console.log the age of my mum and my dad. My mum is twice my age, and my dad is 1.2 the age of my mum.
  4. Call the function.*/

function ageCategory(myAge){
  const mumAge = myAge * 2;
  const dadAge = mumAge * 1.2;
  // console.log(`My mum's age is ${mumAge} years old`)
  // console.log(`My Dad's age is ${dadAge} years old`)
 
  console.log("My mum's age is:" + mumAge)
  console.log("My Dad's age is:" + dadAge)

}
ageCategory(20)
///////////////////////////////////////////////////////////////////


/* write a javascript function that takes a number as a parameter and throws a custom 'Error' if the number is not an integer.*/

function throwCustomError (n){
  if (!Number.isInteger(n)) {
    throw new Error("Not an integer");
  }
  console.log("Valid integer");
}

try {
  throwCustomError(10);
  throwCustomError(50.1);

}
    
catch(e) {
  console.log("Error:", e.message);
}

finally{
  console.log("👌Thank you!!");
}
 