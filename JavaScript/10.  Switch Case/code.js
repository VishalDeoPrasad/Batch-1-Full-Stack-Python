function calculator(operation){
    let num1 = parseFloat(document.getElementById("n1").value);
    let num2 = parseFloat(document.getElementById("n2").value);

    switch(operation){
        case "+":
            document.getElementById("output").innerText = num1+num2;
            break;
        case "-":
            document.getElementById("output").innerText = num1-num2;
            break;
        case "*":
            document.getElementById("output").innerText = num1*num2;
            break;
        case "/":
            document.getElementById("output").innerText = num1/num2;
            break;
        default:
            document.getElementById("output").innerText = "Invalid Operation";
    }
}