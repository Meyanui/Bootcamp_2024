/* We have an array of students which contains an object with all their notes per subjects:

-> Einstein: { Maths: 17, CIT: 16, Geography: 10, Physics: 14 }
-> Josiane: { Maths: 11, CIT: 10, Geography: 18, Physics: 13 }
-> Guilbert: { Maths: 09, CIT: 13, Geography: 16, Physics: 16 }
-> Valentine: { Maths: 12, CIT: 15, Geography: 17, Physics: 09 }

For each student, calculate their average (final note).*/


// Create an array of students with their notes per subjects
let students = [
  {
      name: "Einstein",
      notes: { Maths: 17, CIT: 16, Geography: 10, Physics: 14 }
  },
  {
      name: "Josiane",
      notes: { Maths: 11, CIT: 10, Geography: 18, Physics: 13 }
  },
  {
      name: "Guilbert",
      notes: { Maths: 9, CIT: 13, Geography: 16, Physics: 16 }
  },
  {
      name: "Valentine",
      notes: { Maths: 12, CIT: 15, Geography: 17, Physics: 9 }
  }
];

// Function to calculate the average of an object containing subject grades
function calculateAverage(notes) {
  let subjects = Object.values(notes);
  let total = subjects.reduce((acc, grade) => acc + grade, 0);
  return total / subjects.length;
}

// Calculate and display the average for each student
students.forEach(student => {
  const average = calculateAverage(student.notes);
  console.log(`${student.name}'s average grade is: ${average.toFixed(2)}`);
});
