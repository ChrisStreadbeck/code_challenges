//find the median of an array

function median(numbers) {
  var median = 0;
  numsLen = numbers.length;
  numbers.sort();

  if (numsLen % 2 === 0) {
    median = (numbers[numsLen / 2 - 1] + numbers[numsLen / 2]) / 2;
  } else {
    median = numbers[(numsLen - 1) / 2];
  }

  return median;
}

console.log(median([3, 5, 4, 4, 1, 1, 2, 3]));
