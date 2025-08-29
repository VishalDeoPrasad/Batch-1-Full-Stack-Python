emp2 = {
    'fname': 'Vishal',
    'lname': 'Kumar',
    'age' : 30,
    'address': 'Hyd',
    'phone' : 919876543210,
}
emp1 = emp2.copy()

emp1['phone'] = 1000000000

print(emp1)
print(emp2)