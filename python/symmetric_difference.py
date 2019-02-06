# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
a = set(map(int, raw_input().split()))
M = int(raw_input())
b = set(map(int, raw_input().split()))

exc = (a.difference(a.intersection(b))).union(b.difference(b.intersection(a)))

for e in sorted(exc):
    print(e)
