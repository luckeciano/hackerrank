import numpy


N, M, P = map(int, raw_input().split())

m1 = []
m2 = []
for _ in range(N):
    l = map(int, raw_input().split())
    m1.append(l)

for _ in range(M):
    l = map(int, raw_input().split())
    m2.append(l)

print(numpy.concatenate((m1, m2), axis = 0))