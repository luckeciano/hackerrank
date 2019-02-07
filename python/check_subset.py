# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for t in range(T):
    a = int(raw_input())
    A = set(map(int, raw_input().split()))
    b = int(raw_input())
    B = set(map(int, raw_input().split()))
    print(A.issubset(B))
