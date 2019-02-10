import numpy as np

np.set_printoptions(legacy='1.13')

N, M = map(int, raw_input().split())

mat = []
for _ in range(N):
    mat.append(map(int, raw_input().split()))

mat = np.array(mat)
print(np.mean(mat, axis=1))
print(np.var(mat, axis=0))
print(np.std(mat, axis=None))

