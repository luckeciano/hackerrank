# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(raw_input())
list_shoes = map(int, raw_input().split())
N = int(raw_input())

dict_shoes = Counter(list_shoes)

total = 0
for i in range(N):
    shoe, value = map(int, raw_input().split())
    if shoe in dict_shoes and dict_shoes[shoe] > 0:
        total += value
        dict_shoes[shoe] -= 1
print(total)