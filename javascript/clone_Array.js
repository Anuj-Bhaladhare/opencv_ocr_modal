//clone of array

let fruit=["item1","item2"];
// let fruit2=["item1","item2"]; first approach
// let fruit2=fruit.slice(0).concat(["item3", "item4"]);//second approach
// let fruit2=[].concat(fruit);
fruit.push("item3");
// fruit2.push("itme3");
// fruit2.push("item4");
// console.log(fruit==fruit2);
 console.log(fruit);
//  console.log(fruit2);
 
 //new way to clone of array
 //spread operator
 let oneMoreArray=["item3","itme4"];
let fruit2=[...fruit,...oneMoreArray];
// fruit2.push("item4");
console.log(fruit2);



//how to concatenate two array