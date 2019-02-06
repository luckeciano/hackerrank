# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
a = set(map(int, raw_input().split()))
m = int(raw_input())
b = set(map(int, raw_input().split()))

print (len(a | b))
