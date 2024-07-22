// Function to prompt for expense details and calculate the total expenditure
function calculateExpenditures() {
  
  // Define the dates
  const startDate = prompt("Enter the start date (YYYY-MM-DD):");
  
  const endDate = prompt("Enter the start date (YYYY-MM-DD):");
  
  const totalDays = (endDate - startDate) / (1000 * 60 * 60 * 24) + 1; // Including both start and end dates

  // Prompt for expenses
  const tuitionFee = parseFloat(prompt("Amount of tuition fee paid? : "));
  const transportationPerDay = parseFloat(prompt("Enter the daily transportation cost: "));
  const lunchPerDay = parseFloat(prompt("Enter the daily lunch cost: "));
  const internetSubscription = parseFloat(prompt("Enter the internet subscription cost: "));

  // Calculate total expenses
  const totalTransportation = transportationPerDay * totalDays;
  const totalLunch = lunchPerDay * totalDays;

  const totalExpenditures = tuitionFee + totalTransportation + totalLunch + internetSubscription;

  // Display the results
  alert(`Expenditure Details from ${startDate} to ${endDate}:`);
  alert("Total tuition fee: $" + tuitionFee.toFixed(2));
  alert("Total transportation cost: $" + totalTransportation.toFixed(2));
  alert("Total lunch cost: $" + totalLunch.toFixed(2));
  alert("Internet subscription cost: $" + internetSubscription.toFixed(2));
  alert("Total expenditures: $" + totalExpenditures.toFixed(2));
}

// Call the function to calculate expenditures
calculateExpenditures();
