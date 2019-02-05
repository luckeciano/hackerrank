# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, raw_input().split())
d = defaultdict(list)
for i in range(n):
    el = (raw_input())
    d[el].append(i+1)

for i in range(m):
    el = (raw_input())
    if el not in d:
        print(-1)
    else:
        print ' '.join(str(p) for p in d[el])
