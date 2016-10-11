def mysum(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print mysum(1, 2, 3, 4, 5)
