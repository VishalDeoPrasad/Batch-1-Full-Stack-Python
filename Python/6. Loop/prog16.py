username = "admin"
password = "1234"

uname = input("Enter Username:") 
pwd = input("Enter Password:")

if username == uname and pwd == password:
    print("Login Successful!")
else:
    print("Invalid Username and Password!")