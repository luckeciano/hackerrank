# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())
A = set(map(int, raw_input().split()))
m = int(raw_input())
for i in range(m):
    op = raw_input().split()[0]
    B = set(map(int, raw_input().split()))
    if op == 'intersection_update':
        A.intersection_update(B)
    elif op == 'update':
        A.update(B)
    elif op == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    elif op == 'difference_update':
        A.difference_update(B)
print(sum(A))
