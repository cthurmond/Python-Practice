def mysum(*args):
    # *** HIS CODE ***
    if not args: #checks to see if we actually got arguments
        return args
    output = type(args[0])()
    for arg in args:
        output += arg
    return output

    # *** MY CODE ***

    #if isinstance(args[0], str):
        #total_sum = ''
    #elif isinstance(args[0], list):
        #total_sum = []
    #elif isinstance(args[0], (int, float, long, complex)):
        #total_sum = 0
    
    #for arg in args:
       # total_sum += arg
   # return total_sum

print mysum('abc', 'def')
print mysum([1, 2, 3], [4, 5, 6])
print mysum(1, 2, 3)
