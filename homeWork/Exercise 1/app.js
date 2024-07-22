console.log(document);

//Create a variable which will get each item that you've created inside the list.
let item1 = document.querySelector('.item_1');
let item2 = document.querySelector('.item_2');
let item3 = document.querySelector('.item_3');

//Print them  out using console.log()
console.log(item1.textContent)
console.log(item2.textContent)
console.log(item3.textContent)

//For the last element, change the fontSize to be 24px and the color to be purple.
let items = document.querySelectorAll('li');
// item3.style.fontSize = '24px';
// item3.style.color = 'purple';

item3.setAttribute('style', 'color: purple; font-size: 28px; background-color: red;');

//For the activity you like the most amongst the 03
console.log("The activity I like the most is " + item3.textContent);

