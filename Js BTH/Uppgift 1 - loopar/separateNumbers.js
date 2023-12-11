
//separateNumbers.js

function separateNumbersForLoop(arr) {
  const evenArr = [];
  const oddArr = [];

  //gör en for-loop som placerar jämna tal i evenArr
  //och udda tal i oddArr
  for (let i = 0; i < arr.length; i++)
  {
    if (arr[i] % 2 === 0) {
      evenArr.push(arr[i]);
    } else {
      oddArr.push(arr[i]);
    }
  }    
  return [evenArr, oddArr];
}

/*
implementera funktionerna separateNumbersWhileLoop och  separateNumbersDoWhileLoop.
bägge dessa funktioner ska göra samma sak som separateNumbersForLoop fast med en 
while-loop respektive en Do-While-loop.

implementera också printArray som endast skriver ut innehållet, i konsollen, i arrayen (parameter) med
en foreach-loop.
*/

function separateNumbersWhileLoop(arr) {
  const evenArr = [];
  const oddArr = [];
  let i = 0;
  while (i < arr.length) {
	if (arr[i] % 2 === 0) {
	  evenArr.push(arr[i]);
	} else {
	  oddArr.push(arr[i]);
	}
	i++;
  }
  return [evenArr, oddArr];
}

function separateNumbersDoWhileLoop(arr) {
  const evenArr = [];
  const oddArr = [];
  let i = 0;
  do {
	if (arr[i] % 2 === 0) {
	  evenArr.push(arr[i]);
	} else {
	  oddArr.push(arr[i]);
	}
	i++;
  } while (i < arr.length);
  return [evenArr, oddArr];
}  

function printArray(arr) {
	  arr.forEach(element => console.log(element));
}

module.exports = {
  separateNumbersForLoop,
  separateNumbersWhileLoop,
  separateNumbersDoWhileLoop,
  printArray,
};

