//array destructuring
let array=["value1","value2","value3","value4","value5"];
// let var1=array[0];
// let var2=array[1];
// console.log(var1);
// console.log(var2);
// array destructuring
let [myvalue1,myvalue2, ...myArray]=array;
// let myArray=array.slice(2)
console.log(myvalue1);
console.log(myvalue2);
console.log(myArray);