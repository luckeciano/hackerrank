cube = lambda x: pow(x,3) # complete the lambda function 

def fibonacci(n):
    res = []
    if (n == 0):
        return res
    res.append(0)
    if (n == 1):
        return res
    res.append(1)
    if (n == 2):
        return res

    for k in range(2, n):
        res.append(res[k - 1] + res[k - 2])
    return res
    
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))