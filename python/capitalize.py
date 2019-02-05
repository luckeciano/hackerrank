

# Complete the solve function below.
def solve(s):
    lastChar = False
    for idx in range(len(s)):
        if s[idx] != ' ' and lastChar == False:
            lastChar = True
            s = s[:idx] + s[idx].upper() + s[idx + 1: ]
        elif s[idx] == ' ':
            lastChar = False
    return s



