# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
regex_pattern = r"(?<!^)(#(?:[\da-fA-F]{3}){1,2})"

N = int(raw_input())
for i in range(N):
    st = raw_input()
    m = re.findall(regex_pattern, st)
    if len(m):
        print('\n'.join(m))
