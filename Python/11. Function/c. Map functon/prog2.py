lst = [1,2,3,4,5,6,7,8,9]

def func(n):
    return n+100

print(list(map(func, lst)))