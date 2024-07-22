
// // //Create a stuctured html file linked to a JS file

// // // 1. Create an object that has properties "username" and "password". Fill those values in with strings.

// // // 2. Create an array which contains the object you have made above and name the array "database".

// // // 3. Create an array called "newsfeed" which contains 3 objects with properties "username" and "timeline".

// // let user = {
// //   username : "meyanui",
// //   password : "lilafac",
// // };

// // let database = [user]
// // // const users = ["Josmingo", "Milano", "Nkemio", "Valentina", "Elodia"]


// // let newsfeed = [
// //   {
// //       username: "Josmingo",
// //       timeline: "The Lord is my shepherd"
// //   },
// //   {
// //       username: "Milano",
// //       timeline: "Coding is back stretching."
// //   },
// //   {
// //       username: "Nkemio",
// //       timeline: "The weather in Yaounde is helele!"
// //   }
// // ];

// // console.log(newsfeed);

// // //To access and print a particular "Nkemio"
// // console.log(newsfeed[2].username);


// //Conditionals

// // let age = prompt("Kindly enter your age here")

// // if (age < 18){
// //     alert("Sorry, you are too young to drive this car. Powering off")
// // }
// //   else if (age == 18){
// //     alert("Congratulations on your first year of driving. Enjoy the ride!")
// //  }
// //   else if (age > 18){
// //     alert("Powering On. Enjoy the ride!")
// //  }
// //   else {
// //     alert("Invalid value, add a valid one!")
// //   };
// ////////////////////////////////////////////////////////////////

// // Using the Switch Method
// let age = prompt("Input your age")
// // let age = Number(user_age)

// switch (true){
//   case age < 18:
//     alert("Sorry, you are too young to drive this car. Powering off")
//     break
//   case age === 18:
//     alert("Congratulations on your first year of driving. Enjoy the ride!")
//     break
//   case age > 18:
//     alert("Powering On. Enjoy the ride!")
//     break
//   default:
//     alert("Invalid value, add a valid one!")
// }

//Other exercises
//Exercises on Objects
  // Create a Person Object
  // Create an object person with properties firstName, lastName, age, and profession.
  // Display each property in the console.
  ///////////////////////////////////////////////////////////////////////////////////////

// Create the person object
let person = {
  firstName: "Meyanui",
  lastName: "Valentino",
  age: 36,
  profession: "Software Developer"
};

// To display each property in the console
console.log("First Name:", person.firstName);
console.log("Last Name:", person.lastName);
console.log("Age:", person.age);
console.log("Profession:", person.profession);
//////////////////////////////////////////////////////////////////////////////

//Add and Modify Properties
  // Add a property city to the person object.
  // Modify the profession property to change the profession.
  // Delete the age property.

  // Create the person object    
let person = {
  firstName: "Vina",
  lastName: "Meya",
  age: 30,
  profession: "Content Creator"
};

person.city = "Yaoundé"; // Add a property 'city' to the person object

person.profession = "Data Scientist"; // Modify the 'profession' property

delete person.age; // Delete the 'age' property

// Display the updated properties in the console
  // console.log("First Name:", person.firstName);
  // console.log("Last Name:", person.lastName);
  // console.log("City:", person.city);
  // console.log("Profession:", person.profession);
  // console.log("Age:", person.age);  // Undefined because the age property is deleted
console.log(person)
//////////////////////////////////////////////////////////////////////////////////

//Methods of an Object
  // Add a method introduce to the person object that returns a string introducing the person.
  // Call the method and display the result in the console.

// Create the person object
let person = {
  firstName: "Valentino",
  lastName: "Meyanui",
  profession: "Data Scientist",
  city: "Yaounde",

  // Add the introduce method
  introduce: function() {
      return `Hi, my name is ${person.firstName} ${person.lastName}. I am a ${person.profession} living in ${person.city}.`;
  }
};

// Call the introduce method and display the result in the console
let introduction = person.introduce();
console.log(introduction);
/////////////////////////////////////////////////////////////////////

//Create an Array of Numbers
  // Create an array named numbers containing the numbers from 1 to 10.
  // Display the first and last element of the array.
// Create the array named 'numbers' containing the numbers from 1 to 10
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

console.log("First element:", numbers[0]); // To display the first element
console.log("Last element:", numbers[numbers.length - 1]); // To display the last element


// Create the array named 'numbers' containing the numbers from 1 to 10
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Add the numbers 11 and 12 to the end of the array
numbers.push(11);
numbers.push(12);

// Remove the first element of the array
numbers.shift();

// Reverse the order of the elements in the array
numbers.reverse();

// Display the modified array
console.log(numbers);

// Arrays of Objects
  // Create an array named students containing three objects representing students. 
  // Each object should have the properties name, age, and grade.
  // Display the name and grade of the second student.

// Create the array named 'students' containing three objects representing students
let students = [
  {
      name: "Jumia",
      age: 20,
      grade: "A"
  },
  {
      name: "Bogima",
      age: 22,
      grade: "B"
  },
  {
      name: "Champion",
      age: 21,
      grade: "A"
  }
];

// Display the name and grade of the second student
console.log("Name of the second student:", students[1].name);
console.log("Grade of the second student:", students[1].grade);

//Simple Conditions
  //Ask the user to enter a number. If the number is even, display "Even number"; otherwise, display "Odd number".

// Ask the user to enter a number
let userInput = prompt("Please enter a number:");

let number = Number(userInput); // Convert the input to a number

// Check if the number is even or odd and display the appropriate message
if (number % 2 === 0) {
    alert("Even number");
} else {
    alert("Odd number");
}
////////////////////////////////////////////////////////////////////////////////
// Multiple Case Conditions
  // Ask the user to enter a grade between 0 and 20. Display a message based on the grade:
  // 0-9: "Insufficient"
  // 10-14: "Passable"
  // 15-18: "Good"
  // 19-20: "Excellent"

// Ask the user to enter a grade between 0 and 20
let userInput = prompt("Please enter a grade between 0 and 20:");

// Convert the input to a number
let grade = Number(userInput);

// Display a message based on the grade
if (grade >= 0 && grade <= 9) {
    alert("Insufficient");
} else if (grade >= 10 && grade <= 14) {
    alert("Passable");
} else if (grade >= 15 && grade <= 18) {
    alert("Good");
} else if (grade >= 19 && grade <= 20) {
    alert("Excellent");
} else {
    alert("Invalid grade. Please enter a number between 0 and 20.");
}
///////////////////////////////////////////////////////////////////////

//Combining Objects and Conditions
  // Create an object car with properties brand, model, and year.
  // Ask the user to enter a year. If the year is greater than or equal to the car's year, display "Your car is recent"; otherwise, display "Your car is old".

// Create the car object with properties brand, model, and year
let car = {
  brand: "Toyota",
  model: "Corolla",
  year: 2015
};

// Ask the user to enter a year
let userInfo = prompt("Please enter a year:");

// Convert the input to a number
let userYear = Number(userInfo);

// Compare the entered year with the car's year and display the appropriate message
if (userYear >= car.year) {
  alert("Your car is recent");
} else {
  alert("Your car is old");
}

//To-Do List
  // Create an array named tasks containing objects representing tasks. Each object should have the properties title and completed (boolean).
  // Display all the incomplete tasks.
// Create the array named 'tasks' containing objects representing tasks
const tasks = [
  {
      title: "Do laundry",
      completed: false
  },
  {
      title: "Complete assignment",
      completed: true
  },
  {
      title: "Go grocery shopping",
      completed: false
  },
  {
      title: "Clean the house",
      completed: true
  },
  {
      title: "Pay bills",
      completed: false
  }
];

// Display all the incomplete tasks
console.log("Incomplete tasks:");
tasks.forEach(task => {
  if (!task.completed) {
      console.log(task.title);
  }
});

//Grading System
  // Create an array of objects named courses where each object represents a course with properties name and grade.
  // Calculate the average grade of all the courses.
  // Display a message indicating whether the student has passed (average ≥ 10) or failed.


// Create the array named 'courses' containing objects representing courses
let courses = [
  {
      name: "Mathematics",
      grade: 12
  },
  {
      name: "English",
      grade: 8
  },
  {
      name: "History",
      grade: 15
  },
  {
      name: "Science",
      grade: 10
  },
  {
      name: "Art",
      grade: 14
  }
];

// Calculate the average grade of all the courses
let totalGrade = 0;
courses.forEach(course => {
  totalGrade += course.grade;
});

let averageGrade = totalGrade / courses.length;

// Display a message indicating whether the student has passed or failed
if (averageGrade >= 10) {
  console.log(`The student has passed with an average grade of ${averageGrade.toFixed(2)}.`);
} else {
  console.log(`The student has failed with an average grade of ${averageGrade.toFixed(2)}.`);
}

