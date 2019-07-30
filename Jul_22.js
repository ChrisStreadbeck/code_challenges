// removes the first and last elements in an array

toRemove = ["a", "b", "c", "d"];

function remover(array) {
  return array.slice(1, -1);
}

console.log(remover(toRemove));
