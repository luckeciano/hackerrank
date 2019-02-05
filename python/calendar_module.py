# Enter your code here. Read input from STDIN. Print output to STDOUT
from calendar import weekday

MM, DD, YYYY = map(int, raw_input().split())

day_name = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

print(day_name[weekday(YYYY, MM, DD)])