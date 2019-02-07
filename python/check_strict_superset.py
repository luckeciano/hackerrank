# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, raw_input().split()))
N = int(raw_input())
res = True
for i in range(N):
    B = set(map(int, raw_input().split()))
    if B.issubset(A) and not A.issubset(B):
        res = True
    else:
        res = False
        break
print(res)