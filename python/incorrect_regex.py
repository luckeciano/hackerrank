# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(raw_input())

for i in range(N):
    rg = raw_input()
    try:
        re.compile(rg)
        print(True)
    except re.error:
        print(False)
