import numpy as np

N, M = map(int, raw_input().split())
A = []
B = []
for _ in range(N):
    l = map(int, raw_input().split())
    A.append(l)
for _ in range(N):
    l = map(int, raw_input().split())
    B.append(l)
A = np.array(A)
B = np.array(B)

print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A%B)
print(A**B)

