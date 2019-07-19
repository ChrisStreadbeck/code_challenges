// check to see if a word is a palindrome
const strng = "Hello";
const strng2 = "maam";

function reverser(str) {
  flipped = str
    .split("")
    .reverse()
    .join("");
  if (flipped == str) {
    return "Palindrome";
  } else {
    return "not a Palindrome";
  }
}

console.log(reverser(strng));
console.log(reverser(strng2));

//-----------------------------------------
// removes the first and last elements in an array

toRemove = ["a", "b", "c", "d"];

function remover(array) {
  return array.slice(1, -1);
}

console.log(remover(toRemove));
