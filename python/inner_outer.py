import numpy as np

A = map(int, raw_input().split())
B = map(int, raw_input().split())

print(np.inner(A,B))
print(np.outer(A,B))



