def remove_rep(string):
    s = set()
    res = ''
    for a in string:
        if a not in s:
            s.add(a)
            res += a
    return res

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        print(remove_rep(string[i:i+k]))

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
    