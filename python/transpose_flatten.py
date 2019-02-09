import numpy
matrix = []
N, M = map(int, raw_input().split())

for _ in range(N):
    l = map(int, raw_input().split())
    matrix.append(l)
np = numpy.array(matrix)
print(np.transpose())
print(np.flatten())


