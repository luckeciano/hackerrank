import math
# Enter your code here. Read input from STDIN. Print output to STDOUT
AB = float(raw_input())
BC = float(raw_input())

print (str(int(round(math.degrees(math.atan(AB/BC))))) + "°")
