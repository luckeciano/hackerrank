# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
T, tup = int(raw_input()), raw_input()
Student = namedtuple('Student', tup)
tup = tup.split()
total = 0
for i in range(T):
    a, b, c, d = raw_input().split()
    st = Student(a, b, c, d)
    total += float(st.MARKS)
mean = float(total/T)
print("%.2f" % mean)




