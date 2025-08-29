employee = {
    'fname': 'Vishal',
    'lname': 'Kumar',
    'age' : 30,
    'address': 'Hyd',
    'phone' : 919876543210,
}

# print(employee['first_name'])
print(employee.get('first_name', "Key not found"))