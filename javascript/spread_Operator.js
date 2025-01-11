//spread Operator

// const array=[1,2,3];
// const array1=[4,5,6];

// let myArray=[...array1,...array,7,8,9];
// console.log(myArray);

// const array2=[ ..."123456789"];
// console.log(typeof array2);

//spread Operator in Object
let obj={
    key1:"Value1",
    key2:"Value2",
}
let obj2={
    key1:"Value6",
    key3:"Value3",
    key4:"Value4",

}

// let newObject={...obj2,...obj,key69:"Value69"};
const newObject={...["item1","item2"]};
console.log(newObject);

const alpha={..."abcdefghijklmnopqrstuvwxyz"};
console.log(alpha);


