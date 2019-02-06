# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())
s = set()
for i in range(N):
    st = raw_input()
    s.add(st)
print(len(s))