let room = {
    101: { name: "Vishal", age: 29, phone: '983489834', city: 'hyd'},
    102: { name: "Amit", age: 19, phone: '983489834', city: 'bgl'},
    103: { name: "Rahul", age: 29, phone: '983489834',city: 'hyd'},
};

// add a new guest
room[104] = {
    name: "ABC",
    age: 20,
    phone: "129398345",
    city: "delhi"
};

// update a guest record
room[103].city = "bgl";

// Guest Left
delete room[102];
console.log(room);
