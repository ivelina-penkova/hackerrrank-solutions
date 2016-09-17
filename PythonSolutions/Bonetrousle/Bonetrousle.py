def sum(l, r):
    return r * (r + 1) // 2 - l * (l - 1) // 2

t = int(input())
while t > 0:
    t -= 1
    
    n, k, b = map(int, input().split())

    if sum(1, b) > n or sum(k - b + 1, k) < n: print(-1)
    else:
        a = []
        while n > 0:
            x = min(k, n - sum(1, b - 1))
            a += [x]

            k = x - 1
            b -= 1
            n -= x
        
        print(' '.join(map(str, a)))