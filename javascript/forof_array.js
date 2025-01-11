// for of loop on array
//for of loop is return the element in the array
// let fruits=["apple","banana","mango"];
// let array2=[];
// for(let fruit of fruits){
//     array2.push(fruit.toUpperCase());
// }
// console.log(array2);

//for in loop on array
//for in loop return the index in that array
let fruits=["apple","banana","mango"];
let array2=[];
for(let fruit in fruits){
    array2.push(fruits[fruit].toUpperCase());
}
console.log(array2);    