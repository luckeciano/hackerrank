# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(raw_input())

pattern = re.compile('[-+]?[0-9]*\.[0-9]*.')

for _ in range(N):
    a = raw_input()
    if bool(pattern.match(a)):
        try:
            a = float(a)
            print True
        except:
            print False
    else:
        print False