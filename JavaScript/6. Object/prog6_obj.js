let person = {
    f_name : "Vishal",
    s_name : "Kumar",
    full_name: function(){
        return this.f_name + " " + this.s_name;
    }
};

console.log(person.full_name());