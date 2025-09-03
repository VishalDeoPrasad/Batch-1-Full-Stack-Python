try:
    x = int(input("Enter a number: "))
    ans = 10/x
    print(ans)
except ZeroDivisionError:
    print("Cannot divide by Zero:")
except ValueError:
    print("You can not put string value:")