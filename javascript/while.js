//while loop
//print the number 0 to 9 

// let i=0;
// while(i<=9){
//     console.log(i);
//     i++;
// }
// console.log(`Current value of i is ${i}`);

// first 10 natural number sum first approach
let i=0;
let sum=0;
while(i<=10){
    sum+=i;
    i++;
  
}
console.log(sum);

//2nd approach fast approach
let num=10;
let total=(num*(num +1))/2;
console.log(total);