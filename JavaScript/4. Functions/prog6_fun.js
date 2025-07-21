function even_odd_checker(n){
    if (n % 2 == 0){
        return "Even";
    }
    else{
        return "Odd";
    }
}

ans = even_odd_checker(10);
console.log(ans);