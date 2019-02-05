if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr = sorted(arr)
    maxScore = arr[n - 1]
    for i in reversed(range(n)):
        if arr[i] < maxScore:
            print(arr[i])
            break

