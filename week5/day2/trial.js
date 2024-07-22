// Define variables with your address details
let addressNumber = 5;
let addressStreet = "BenYehuda";
let country = "Israel";

// Concatenate variables to form a complete address sentence
let globalAddress = "I live in " + addressNumber + " " + addressStreet + ", " + country + ".";

// Get the paragraph element with ID "address-output"
const addressOutput = document.getElementById("address-output");

// Set the content of the paragraph element to the globalAddress variable
addressOutput.textContent = globalAddress;


