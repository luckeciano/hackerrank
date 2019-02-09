import numpy

def arrays(arr):
    arr.reverse()
    return numpy.array(arr, float)
    # complete this function
    # use numpy.array

arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)