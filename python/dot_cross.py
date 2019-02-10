import numpy as np

N = int(raw_input())
A = []
B = []
for _ in range(N):
    A.append(map(int, raw_input().split()))


for _ in range(N):
    B.append(map(int, raw_input().split()))

A = np.array(A)
B = np.array(B)

print(np.dot(A,B))

