let unit = 310;
let bill = 0

if (unit<=100){
    bill = unit*1.5;
}

else if (unit <= 200){
    bill = (100 * 1.5) + (unit - 100) * 2.0;
}

else if (unit <= 300){
    bill = (100 * 1.5) + (100 * 2.0) + (unit - 200) * 2.5;
}

else{
    bill = (100 * 1.5) + (100 * 2.0) + (100 * 2.5) + (100 * 3.0) + (unit - 400) * 5;
}

console.log("Bill Amount: ", bill)