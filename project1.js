let students = ["Amit", "Rahul", "Ruhi", "Anjali", "Vishal"];
let marks = [93, 67, 90, 43, 99];

for (let i=0; i<5; i++){
    if (marks[i] >= 90){
        console.log(students[i],marks[i],"Excellent");
    }
    else if (marks[i] >= 75){
        console.log(students[i],marks[i],"Good");
    }
    else if (marks[i] >= 60){
        console.log(students[i],marks[i],"Average");
    }
    else if (marks[i] >= 45){
        console.log(students[i],marks[i],"Below Average");
    }
    else{
        console.log(students[i],marks[i],"Fail");
    }
}