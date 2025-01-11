//intro to array
//array is an refrence type
let fruit=["apple","banana","pineapple","Orange"];
console.log(fruit);
fruit[1]="mango";
console.log(fruit);

let number=[22,35,"hindi",undefined, null,2.030];
console.log(typeof number);
console.log(Array.isArray(number));//isArray is method to check the given array is an array

//Ordered collection of item it is called array

let object={

};
console.log(Array.isArray(object));