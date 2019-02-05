if __name__ == '__main__':
    res = []
    N = int(raw_input())
    for _ in range(N):
        op = raw_input().split()
        if len(op) == 3:
            idx, el = int(op[1]), int(op[2])
            res.insert(idx, el)
        elif op[0] == 'print':
            print(res)
        elif op[0] == 'remove':
            e = int(op[1])
            for el in res:
                if el == e:
                    res.remove(el)
                    break
        elif op[0] == 'append':
            el = int(op[1])
            res.append(el)
        elif op[0] == 'sort':
            res = sorted(res)
        elif op[0] == 'pop':
            res.pop()
        elif op[0] == 'reverse':
            res.reverse()


