import numpy as np
from sklearn.linear_model import LinearRegression

F_N = (raw_input()).split()
F = int(F_N[0])
N = int(F_N[1])


total_features =[]
Y = []
for n in range(N):
    x_y = map(float, raw_input().rstrip().split())
    feature_list = []
    for i in range(F):
        feature_list.append(x_y[i])
    total_features.append(feature_list)
    Y.append(x_y[F])

tc = int(raw_input())
features_tc = []
for i in range(tc):
    ft_tc = map(float, raw_input().rstrip().split())
    features_tc.append(ft_tc)

reg = LinearRegression().fit(total_features, Y)
y_test = reg.predict(features_tc)

for y in y_test:
    print(y)