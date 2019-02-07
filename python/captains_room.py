# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
K = int(raw_input())
l = map(int, raw_input().split())

c = Counter(l)
for tup in c.items():
    if tup[1] != K:
        print(tup[0])

