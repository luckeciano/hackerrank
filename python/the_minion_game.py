def count_substrings(idx, string):
    res = 0
    return len(string) - idx

def minion_game(string):
    # your code goes here
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in "AEIOU":
            kevin += count_substrings(i, string)
        else:
            stuart += count_substrings(i, string)
    if kevin > stuart:
        print("Kevin " + str(kevin))
    elif kevin == stuart:
        print("Draw")
    else:
        print("Stuart " + str(stuart))

