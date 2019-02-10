def wrapper(f):
    def fun(l):
        # complete the function
        for k in range(len(l)):
            i = l[k]
            l[k] = "+91 " + i[-10:-5] + " " + i[-5:]
        l = f(l)
    return fun

@wrapper
def sort_phone(l):
    print '\n'.join(sorted(l))

if __name__ == '__main__':
    l = [raw_input() for _ in range(int(input()))]
    sort_phone(l) 