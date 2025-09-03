try:
    x = int(input("Enter a number: "))
    ans = 10/x
    print(ans)
except (ZeroDivisionError, ValueError) as e:
    print(e)