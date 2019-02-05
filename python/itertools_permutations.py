# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

inp = raw_input().split()
string = inp[0]
k = int(inp[1])

perm = sorted(permutations(string, k))

for p in perm:
    print(''.join(p))
