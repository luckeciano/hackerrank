N, M = map(int, raw_input().split())

for i in range(N // 2):
    line = '-' * ((M - 3*(2*i + 1)) // 2) + '.|.' * (2*i + 1) + '-' * ((M - 3*(2*i + 1)) // 2)
    print(line)

line = '-' * ((M - 7) // 2) + 'WELCOME' + '-' * ((M - 7) // 2)
print(line)

for i in reversed(range(N // 2)):
    line = '-' * ((M - 3*(2*i + 1)) // 2) + '.|.' * (2*i + 1) + '-' * ((M - 3*(2*i + 1)) // 2)
    print(line)