try:
    x = int(input("Enter a number: "))
    ans = 10/x
    print(ans)

except Exception as e:
    print(e)

else:
    print("I'm Else Block!")

finally:
    print("I'm Finally block!")