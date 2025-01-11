//how to iterate object
let object={
    name:"harsh",
    age:20,
    city:"Nagpur",
   "person hobbies":["singing","dancing","cooking","cricket"],
    
};

// forin loop
// object.keys

// for(let key in object){
//     // console.log(key,":",object[key]);
//     console.log(`${key}:${object[key]}`)
// }

// console.log(typeof Object.keys(object));
// const val=Array.isArray(Object.keys(object));
// console.log(val);

for(let k of Object.keys(object)){
    console.log(object[k]);
}