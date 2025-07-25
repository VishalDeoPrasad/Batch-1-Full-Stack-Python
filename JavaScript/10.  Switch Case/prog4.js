let n1 = 10;
let n2 = 20;

function calculator(operation){
    switch(operation){
        case "+": 
            console.log(n1+n2);
            break;
        case "-":
            console.log(n1-n2);
            break;
        case "*":
            console.log(n1*n2);
            break;
        case "/":
            console.log(n1/n2);
            break;
        default:
            console.log("Invalid Operation!");
    }
}
calculator("+");
calculator("-");
calculator("*");
calculator("/");
calculator("%");