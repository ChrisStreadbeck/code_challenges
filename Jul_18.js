//create an array from a large number

const num = 1234567890;

function number(num) {
  const digits = num.toString().split("");
  return digits;
}

console.log(number(num));
