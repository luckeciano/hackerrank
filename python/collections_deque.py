# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(raw_input())
d = deque()
for i in range(n):
    inp = raw_input().split()
    op = inp[0]
    if op == 'append':
        e = (inp[1])
        d.append(e)
    elif op == 'appendleft':
        e = (inp[1])
        d.appendleft(e)
    elif op == 'pop':
        d.pop()
    elif op == 'popleft':
        d.popleft()
print(' '.join(d))