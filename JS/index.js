age = 20;

if (age > 18) {
    // console.log("you can drink rasna water");
}
else {
    // console.log("you can not drink rasna water");
}

// console.log("end of ladder")

// Arrays[]

// 2 methods to iterate array

var arr = [1, 2, 5, 7, 9];

// for loop

for (var i = 0; i < arr.length; i++) {
    // console.log(arr[i])
}


arr.forEach(function (element) {
    // console.log(element)
});

// while loop

let j = 0;
// while(j<arr.length){
//     // console.log(arr[j]);
//     j++;
// } 

// do while loop

do {
    // console.log(arr[j]);
    j++;
} while (j < arr.length);

// function()

function avg(a, b) {
    return (a + b) / 2;
}

c1 = avg(4, 5);
c2 = avg(5, 6);
// console.log(c1,c2);


let myarr = ["fan", "Camera", 30, null, true]
//Array methods
// console.log(myarr.length);
// myarr.pop();
// myarr.push("new");
// myarr.shift();
// console.log(myarr);

//String Methods in JavaScript

let myString = "new string";
// console.log(myString.length);
let mydate = new Date();
// console.log(mydate);
// console.log(mydate.getTime());
// console.log(mydate.getFullYear);
// console.log(mydate.getHours);
// console.log(mydate.getSeconds);

document.getElementsByTagName("div")
