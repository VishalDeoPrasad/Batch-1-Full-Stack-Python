let kart_value = 600;
let isPremium = false;

let output = (kart_value>=500 || isPremium);
if (output) {
    console.log("You get free delivery!");
}
else{
    console.log("You need to pay delivery charge!");
}