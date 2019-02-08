# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
S, k = raw_input(), raw_input()

matches = list(re.finditer(r'(?={})'.format(k), S))

if matches:
    print('\n'.join(str((match.start(),
          match.start() + len(k) - 1)) for match in matches))
else:
    print('(-1, -1)')