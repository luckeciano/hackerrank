import numpy

N, M = map(int, raw_input().split())
mat = []
for _ in range(N):
    l = map(int, raw_input().split())
    mat.append(l)
print(numpy.prod(numpy.sum(mat, axis=0)))


