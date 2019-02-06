# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

inp = raw_input().split()

e = sorted(inp[0])
N = int(inp[1])
for i in range(1, N + 1):
    l = list(combinations(e, i))
    for p in l:
        print(''.join(p))

