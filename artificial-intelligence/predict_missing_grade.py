# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd
import json


#df = pd.read_json('training.json', lines=True, orient='columns')


courses = ['English', 'Physics', 'Chemistry', 'ComputerScience', 'Hindi', 'Biology', 'PhysicalEducation', 'Economics', 'Accountancy', 'BusinessStudies']

features = []
Y = []

with open('training.json') as f:
    nlines = f.readline()
    for i in range(int(nlines)):
        features_list = []
        js = f.readline()
        js = json.loads(js)
        for course in courses:
            if course in js:
                features_list.append(js[course])
            else:
                features_list.append(0)
        Y.append(js['Mathematics'])
        features.append(features_list)

model = LogisticRegression().fit(features, Y)

features = []
nlines = raw_input()
features = []
for i in range(int(nlines)):
    features_list = []
    js = raw_input()
    js = json.loads(js)
    for course in courses:
        if course in js:
            features_list.append(js[course])
        else:
            features_list.append(0)
    features.append(features_list)
res = model.predict(features)
for i in res:
    print(i)
