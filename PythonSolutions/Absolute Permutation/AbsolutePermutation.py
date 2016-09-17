t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if k == 0: print(' '.join(map(str, range(1, n + 1))))
    elif n % (2 * k) != 0: print(-1)
    else:
        f = []
        for x in range(n // (2 * k)):
            f += list(range(x * 2 * k + k + 1, x * 2 * k + 2 * k + 1)) + list(range(x * 2 * k + 1, x * 2 * k + k + 1))
        
        print(' '.join(map(str, f)))