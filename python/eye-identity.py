import numpy

#solve the problem of space in output
print(str(numpy.eye(*map(int,raw_input().split()))).replace('1',' 1').replace('0',' 0'))




