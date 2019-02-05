# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict


ordered_dictionary = OrderedDict()
N = int(raw_input())
for i in range(N):
    line = raw_input().split()
    name, value = ' '.join(line[:-1]), line[-1]
    if name not in ordered_dictionary.keys():
        ordered_dictionary[name] = int(value)
    else:
        ordered_dictionary[name] += int(value)

for el in ordered_dictionary.keys():
    print(' '.join((el, str(ordered_dictionary[el]))))
