import numpy as np


N, M = map(int, raw_input().split())

A = np.array([map(int, raw_input().split()) for _ in range(N)])

print(np.max(np.min(A, axis=1)))