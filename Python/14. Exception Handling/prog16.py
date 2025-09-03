try:
    x = int(input("Enter a number: "))
    ans = 10/x
    print(ans)
except (ZeroDivisionError, ValueError):
    print("You might enter 0 or you enter any string!")