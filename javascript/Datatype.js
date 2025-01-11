// null
let a=null;
console.log(typeof a);
//bug, error in javascript null type is object
a="harshit";
console.log(a, typeof(a));


// undefined
let name;
console.log(typeof(name)); //prints undefined



// BigInt
let b=BigInt(132);
let c=123n;  //declare BigInt
console.log(b);
console.log(c+b);
console.log(Number.MAX_SAFE_INTEGER);