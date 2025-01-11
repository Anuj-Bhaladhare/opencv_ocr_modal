//Object destructuring
let band={
    bandName:"big banc",
    famousSong:"straway to heaven",
    year:1969,
    anotherFamousSong:"kashmir",
};
// const bandName=band.bandName;
// const famousSong=band.famousSong;
// console.log(bandName,famousSong);
let {bandName,famousSong,...p}=band;
bandName="queen";
// console.log(var2);
// console.log(band);
console.log(p);