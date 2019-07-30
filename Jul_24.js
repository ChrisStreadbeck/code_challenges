// alphabetizes a string

let astring = "this is a string";

function alphabetizes(text) {
  return text
    .split("")
    .sort()
    .join("");
}

console.log(alphabetizes(astring));
