// Insert Commas - Algorithm

/*
Problem:

Write a function that takes in an integer, n,
and returns a string with the correct amount of commas.

Examples:

if n = 1000
function returns '1,000'

if n = 100,000
function returns '100,000'

if n = 1000000
function returns '1,000,000'
*/

// This algorithm assumes there are no decimals in integers
// Note the i !== 0 condition in the if statement, which meets an edge case

function addCommas(n) {
  var str = n.toString() // convert number to string
  var splitString = str.split(''); // split string into array
  var count = 0; // initialize a count variable

  for (var i = splitString.length - 1; i >= 0; i--) {
    count += 1; // increment count by 1

    if (count % 3 === 0 && i !== 0) {
      splitString.splice(i, 0, ','); // insert commas into appropriate indexes
    }
  }

  str = splitString.join(''); // join array into string
  return str;
}

//addCommas(1000);
//addCommas(100000);
//addCommas(1000000);
//addCommas(99999);
