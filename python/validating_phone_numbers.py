# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
pattern = r"[789][0-9]{9}$"
prog = re.compile(pattern)

N = int(raw_input())
for _ in range(N):
    s = raw_input()
    if prog.match(s):
        print "YES"
    else:
        print "NO"

