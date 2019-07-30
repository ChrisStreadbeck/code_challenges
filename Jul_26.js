// FizzBuzz

function FizzBuzz(start, end) {
  for (let i = start; i <= end; i++) {
    if (i % 5 == 0 && i % 3 == 0) {
      console.log("FizzBuzz");
    } else if (i % 5 == 0) {
      console.log("Fizz");
    } else if (i % 3 == 0) {
      console.log("Buzz");
    } else {
      console.log(i);
    }
  }
}
console.log(FizzBuzz(1, 100));
