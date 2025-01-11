//objects refrence type
//array are good but not sufficient
//for real world data
//objects are store key and value pair
//objects don't have an index


//how to create a object
let object={
    name:"harsh",
    age:20,
    city:"Nagpur",
    hobbies:["singing","dancing","cooking","cricket"],
    sing:[]
};

hoby=object.hobbies;
for(let i=0; i<hoby.length;i++){
    object.sing.push(hoby[i]);
}
console.log(object);

//how to access data from the objects

// console.log(object.hobbies);


//how to add key value pair to objects
// object.gender="male";
// console.log(object);