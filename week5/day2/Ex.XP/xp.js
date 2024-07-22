// Exercise 1 - Review About Arrays -  List Of People

// Initial array
const people = ["Greg", "Mary", "Devon", "James"];

// 1. Remove "Greg" from the people array
people.shift();
console.log(people); // ["Mary", "Devon", "James"]

// 2. Replace "James" with "Jason"
const index = people.indexOf("James");
if (index !== -1) {
  people[index] = "Jason";
}
console.log(people); // ["Mary", "Devon", "Jason"]

// 3. Add your name to the end of the people array
people.push("Yourname"); // replace "Yourname" with your actual name
console.log(people); // ["Mary", "Devon", "Jason", "Yourname"]

// 4. Console.log Mary’s index
console.log(people.indexOf("Mary")); // 0

// 5. Make a copy of the people array excluding "Mary" and your name
const newPeople = people.slice(1, -1);
console.log(newPeople); // ["Devon", "Jason"]

// 6. Gives the index of "Foo"
console.log(people.indexOf("Foo")); // -1 because "Foo" is not in the array

// 7. Create a variable called last which is the last element of the array
const last = people[people.length - 1];
console.log(last); // "Yourname"

//***************************************************************************** */

//Exercise 2 - Your Favorite Colors

  // Create an array called colors with your five favorite colors
// Créez un tableau appelé colors avec vos cinq couleurs préférées
const colors = ["blue", "red", "green", "yellow", "purple"];

// Loop through the array and log the string
// Parcourez le tableau et affichez la chaîne
for (let i = 0; i < colors.length; i++) {
  // Log a message with the color and its position
  // Affichez un message avec la couleur et sa position
  console.log(`My #${i + 1} choice is ${colors[i]}`);
}

// Bonus: Change it to log "My 1st choice", "My 2nd choice", "My 3rd choice", etc.
// Bonus : Changez-le pour afficher "My 1st choice", "My 2nd choice", "My 3rd choice", etc.
const suffixes = ["st", "nd", "rd", "th", "th"]; // Suffixes for 1st, 2nd, 3rd, etc.
// Suffixes pour 1er, 2ème, 3ème, etc.

for (let i = 0; i < colors.length; i++) {
  // Determine the correct suffix for the current position
  // Déterminez le suffixe correct pour la position actuelle
  const suffix = (i + 1) <= 3 ? suffixes[i] : suffixes[3];
  // Log a message with the color and its position with the correct suffix
  // Affichez un message avec la couleur et sa position avec le suffixe correct
  console.log(`My ${i + 1}${suffix} choice is ${colors[i]}`);
}

//**************************************************************************/
// Exercise 3 Repeat the question

// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?

let userInput;
do {
  userInput = prompt("Please enter a number:");
  userInput = Number(userInput);  // Convert the input to a number
} while (typeof userInput === 'number' && userInput < 10);

console.log("The final number entered is: " + userInput);


// Exercise 4
// const building = {
//   numberOfFloors: 4,
//   numberOfAptByFloor: {
//       firstFloor: 3,
//       secondFloor: 4,
//       thirdFloor: 9,
//       fourthFloor: 2,
//   },
//   nameOfTenants: ["Sarah", "Dan", "David"],
//   numberOfRoomsAndRent:  {
//       sarah: [3, 990],
//       dan:  [4, 1000],
//       david: [1, 500],
//   },
// }


// Review About Objects
// Copy and paste the above object to your Javascript file.

// Console.log the number of floors in the building.

// Console.log how many apartments are on the floors 1 and 3.

// Console.log the name of the second tenant and the number of rooms he has in his apartment.

// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.

const building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
      firstFloor: 3,
      secondFloor: 4,
      thirdFloor: 9,
      fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent:  {
      sarah: [3, 990],
      dan:  [4, 1000],
      david: [1, 500],
  },
};

// 1. Console.log the number of floors in the building.
console.log("Number of floors in the building:", building.numberOfFloors);

// 2. Console.log how many apartments are on the floors 1 and 3.
console.log("Number of apartments on the 1st floor:", building.numberOfAptByFloor.firstFloor);
console.log("Number of apartments on the 3rd floor:", building.numberOfAptByFloor.thirdFloor);

// 3. Console.log the name of the second tenant and the number of rooms he has in his apartment.
const secondTenant = building.nameOfTenants[1];
const secondTenantRooms = building.numberOfRoomsAndRent[secondTenant.toLowerCase()][0];
console.log("The name of the second tenant:", secondTenant);
console.log("Number of rooms the second tenant has:", secondTenantRooms);

// 4. Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, then increase Dan’s rent to 1200.
const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent = building.numberOfRoomsAndRent.dan[1];

if ((sarahRent + davidRent) > danRent) {
  building.numberOfRoomsAndRent.dan[1] = 1200;
}

console.log("Dan's new rent:", building.numberOfRoomsAndRent.dan[1]);

// Exercise 5 - Family
// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.

const family = {
  father: "John",
  mother: "Jane",
  son: "Mike",
  daughter: "Emily"
};

// Using a for...in loop to console.log the keys of the object
console.log("Keys of the family object:");
for (const key in family) {
  console.log(key);
}

// Using a for...in loop to console.log the values of the object
console.log("Values of the family object:");
for (const key in family) {
  console.log(family[key]);
}

// Exercise 6 - Rudold
// const details = {
//   my: 'name',
//   is: 'Rudolf',
//   the: 'reindeer'
// }
// Given the object above and using a for loop, console.log “my name is Rudolf the reindeer”

const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
};

let sentence = "";

for (const key in details) {
  sentence += key + " " + details[key] + " ";
}

// Remove the trailing space
sentence = sentence.trim();

console.log(sentence);


// Exercise 7 : Secret Group
// Instructions
// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

// Step 1: Extract the first letter of each name
let firstLetters = names.map(name => name.charAt(0));

// Step 2: Sort these letters alphabetically
firstLetters.sort();

// Step 3: Join the sorted letters to form the society’s name
let secretSocietyName = firstLetters.join("");

console.log("The name of the secret society is:", secretSocietyName);
