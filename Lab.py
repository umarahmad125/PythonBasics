def fun(*args):
    total = 0
    for i in args:
        total += i
    return total

print(fun(2,5,5))