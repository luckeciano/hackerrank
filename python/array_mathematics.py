import numpy as np

N, M = raw_input().split()

A = np.array(map(int, raw_input().split()))
B = np.array(map(int, raw_input().split()))

print('[' + str(A+B) + ']')
print('[' + str(A-B) + ']')
print('[' + str(A*B) + ']')
print('[' + str(A/B) + ']')
print('[' + str(A%B) + ']')
print('[' + str(A**B) + ']')


