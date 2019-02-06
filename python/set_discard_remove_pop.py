n = input()
s = set(map(int, raw_input().split()))

m = int(raw_input())

for i in range(m):
    inp = raw_input().split()
    op = inp[0]
    if op == 'pop':
        s.pop()
    elif op == 'remove':
        e = int(inp[1])
        s.remove(e)
    elif op == 'discard':
        e = int(inp[1])
        s.discard(e)

su = 0
for el in s:
    su += el
print(su)
