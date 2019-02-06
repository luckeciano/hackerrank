# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
inp = raw_input().split()
e = sorted(inp[0])
k = int(inp[1])

l = combinations_with_replacement(e, k)
for el in l:
    print(''.join(el))
