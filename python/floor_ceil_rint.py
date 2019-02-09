import numpy as np
np.set_printoptions(sign=' ')
a = np.array(map(float, raw_input().split()))
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))

