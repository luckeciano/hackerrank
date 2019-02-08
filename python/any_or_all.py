# Enter your code here. Read input from STDIN. Print output to STDOUT
def palyndromicInteger(a):
    for i in range(len(a)//2):
        if (a[i] != a[len(a) - 1]):
            return False
    return True

N = int(raw_input())
l = raw_input().split()

print(all(int(a) > 0 for a in l) and any(palyndromicInteger(a) for a in l))