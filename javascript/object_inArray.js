//object inside the array
//very useful in real world

let users=[
    {
        userId:1,
        firstName:"Mohit",
        lastName:"Meshram",
    },
    {
        userId:2,
        firstName:"Rohit",
        lastName:"Sharma",
    },
    {
        userId:3,
        firstName:"Virat",
        lastName:"Kohli",
    }
];

console.log(users[0]);

// for(let user of users){
//     console.log(user);
// }
// console.log(users);
for(let i=0;i<users.length;i++){
   
    if(i==0){
       
        break;
        console.log(users[i]);
    }
    
}