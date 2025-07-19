let student = {
    name: "Vishal",
    roll_no: 12345,
    age: 29,
    marks: 99,
    degree: "Master's",
    phone: '1234xxx567',
    city: "bgl"
};

for (let key in student){
    console.log(student[key]);
}