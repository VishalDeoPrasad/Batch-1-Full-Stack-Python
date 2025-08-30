lst = [4,3,2,6,7,8,4,5,3,1,2,6,4]
# func = lambda n : n % 2 == 0
def func(n):
    return n % 2 == 0
print(list(filter(func, lst)))