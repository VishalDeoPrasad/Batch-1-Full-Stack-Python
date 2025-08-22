username = "admin"
password = "1234"

for i in range(3):
    uname = input("Enter Username:") 
    pwd = input("Enter Password:")

    if username == uname and pwd == password:
        print("Login Successful!")
        break
    else:
        print("Invalid Username and Password!")
        
else:        
    print("Account Locked!")