// @Array_Helper_Functions

// forEach
// map
// filter
// find
// every
// some
// reduce

const nums = [1, 2, 3, 4, 5, 6, 7, 8];

// @forEach
let sum = 0;

nums.forEach((num) => {
  sum += num;
});

console.log(sum); // 36

// @map
const newEvenNumArray = nums.map((num) => {
  return num * 2;
});

console.log(newEvenNumArray); // [ 2,  4,  6,  8, 10, 12, 14, 16]

// @filter
const numsGreaterThan5 = nums.filter((num) => {
  return num > 5;
});

console.log(numsGreaterThan5); // [ 6, 7, 8 ]

// @find
const numTwo = nums.find((num) => {
  return num === 2;
});

console.log(numTwo); // 2

// @every
const isEveryNumEven = nums.every((num) => {
  return num % 2 === 0;
});

console.log(isEveryNumEven); // false

// @some
const areSomeNumsEven = nums.some((num) => {
  return num % 2 === 0;
});

console.log(areSomeNumsEven); // true

// @reduce
const total = nums.reduce((prev, current) => {
  return prev + current;
}, 0);

console.log(total); // 36

// node Javascript/arrayHelperFunctions.js
