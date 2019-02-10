import numpy as np
np.set_printoptions(legacy='1.13')
N = int(raw_input())
n = np.array([map(float, raw_input().split()) for _ in range(N)])

print(np.linalg.det(n))
