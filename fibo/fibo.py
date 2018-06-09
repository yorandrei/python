#def test():
#    fib = [i**2 for i in range (10) if i**2 %2 == 0]
#fib = [i+(i-1) for i in range(6)]
#    print(fib)

def floor(num):
    return int(num)

def ceil(num):
    if num > int(num):
        return int(num+1)
    else:
        return int(num)
