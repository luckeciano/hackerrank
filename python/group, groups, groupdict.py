# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
st = raw_input()
m = re.search(r'([a-zA-Z0-9])\1+', st)
print(m.group(1) if m else -1)