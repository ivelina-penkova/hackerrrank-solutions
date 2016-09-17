def pattern_here(G, row_i, g):
    i = G[row_i].find(g[0])
    while i != -1:
        found = True
        for j in range(1, len(g)):
            if G[row_i + j][i:i+len(g[j])] != g[j]:
                found = False
        if found:
            return True
        i = G[row_i].find(g[0], i+1)
    return False

tests = int(input())

for _ in range(tests):
    R, C = list(map(int, input().split()))
    G = []
    found = False
    for row in range(R):
        G.append(input())
    r, c = list(map(int, input().split()))
    g = []
    for row in range(r):
        g.append(input())
    
    for row_i in range(0, R - r + 1):
        if pattern_here(G, row_i, g):
            found = True
            break
    if found:
        print("YES")
    else:
        print("NO")