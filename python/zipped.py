# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = map(int, raw_input().split())
a = []
for i in range(X):
    a.append(map(float, raw_input().split()))
    
for t in zip(*a):
    print( sum(t)/len(t))
