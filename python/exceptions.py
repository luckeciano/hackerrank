# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())
for t in range(T):
    a,b = raw_input().split()
    try:
        print(int(a)/int(b))
    except ZeroDivisionError as e:
        print("Error Code: " + str(e))
    except ValueError as e:
        print("Error Code: " + str(e))
    