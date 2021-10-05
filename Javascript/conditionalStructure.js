// @Conditional_Structures_In_Javascript

// 01) if statement
// 02) if else statement
// 03) if else-if else statement

// @if_statement
if (true) {
  console.log('inside the if block');
}

// @if_else_statement
if (false) {
  console.log('inside the if block');
} else {
  console.log('inside the else block');
}

// @if_else_if_else_statement

// Example #1
let block;
if (false) {
  block = 'if block';
} else if (true) {
  block = 'else if block';
} else {
  block = 'else block';
}

console.log(block); // else if block

// Example #2 (we can also use the multiple "else if" statements)
let body;
if (false) {
  body = 'if block';
} else if (false) {
  body = 'first else if block';
} else if (true) {
  body = 'second else if block';
} else {
  body = 'else block';
}

console.log(body); // second else if block
