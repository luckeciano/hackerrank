import numpy as np

pol = np.array(map(float, raw_input().split()))
n = float(raw_input())

print(np.polyval(pol, n))


