//trim(),toUpperCase, toLowerCase(),slice
//trim() method is used to remove spaces and generate a new string
let lastName="   Harsh   ";
// console.log(lastName.length);
let newString=lastName.trim();
// console.log(newString.length);


//toUpperCase() methos is used covert the string into capital letters

let string="Harsh";
let capital=string.toUpperCase();
// console.log(capital);

let small=string.toLowerCase();
// console.log(small);
//slice(1,3) 1 is a start index and 3 is end index
let slice=string.slice(1,3);
// console.log(slice);


//typeof operator
let a=22;
// console.log(typeof(a));//number data type

let b=true;
// console.log(typeof(b));//boolean data type

let name="Rakesh";
// console.log(typeof(name));// String data type

let c=null;
// console.log(typeof(c));


//data types :

//string "kohinoor"
//number 2,3,4,5
//Boolean true and false
//null
//undefined
//BigInt
//Symbol



// 1st approach
//convert number to string
let d=25;
d=d+"";
// console.log(typeof(d));



//convert string to number
let newStr=+"34";
// console.log(typeof(newStr));

//2nd approach
let e="24";
e=Number(e)
// console.log(typeof e);



//string Concatenation

//my name is kohinoor and my surname is kamble
// let o= "my name is " + m + "and my surname is  "+ n;
// console.log(o);

let x="20";
let y="35";
let z= +x + +y;
console.log(typeof z);


// template string
let m="Kohinoor";
let n="Kamble";

let p=`my name is ${m} and my surname is ${n}`;
console.log(p);