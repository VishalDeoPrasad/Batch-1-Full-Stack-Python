student = {
    "name": "Vishal",
    "age": 30,
    "address": "Bgl"
}

try:
    print(student['phone'])

except KeyError:
    print("Got the key error!")
