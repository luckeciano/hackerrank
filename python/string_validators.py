if __name__ == '__main__':
    s = raw_input()
    bools = [False, False, False, False, False]
    for c in s:
        bools[0] |= c.isalnum()
        bools[1] |= c.isalpha()
        bools[2] |= c.isdigit()
        bools[3] |= c.islower()
        bools[4] |= c.isupper()
    for bol in bools:
        print(bol)
    
