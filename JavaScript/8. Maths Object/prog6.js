function generateOTP(){
    let otp="";
    for (let i=0; i<6; i++){
        let n = Math.floor(Math.random() * 10);
        otp = otp + n;
    }
    return otp;
}

console.log(generateOTP());
