input()
numberStrList = input().split()
numberList = [int(x) for x in numberStrList]

def canSwapOnce(l):
    d = []
    s = sorted(l)
    for x in range(len(l)):
        if l[x] != s[x]:
            d.append(x)
    if len(d) != 2:
        return False
    else:
        a = l[d[0]]
        l[d[0]] = l[d[1]]
        l[d[1]] = a
        if l == s:
            return d
        else:
            return False
        
def canReverseSegment(l):
    d = []
    s = sorted(l)
    for x in range(len(l)):
        if l[x] != s[x]:
            d.append(x)
    if len(d) > 2:
        p = l[d[0]:d[-1] + 1]
        p.reverse()
        if s == l[0:d[0]] + p + l[d[-1] + 1:]:
            return d
        else: return False
    return False

d = canSwapOnce([int(x) for x in numberStrList])
e = canReverseSegment([int(x) for x in numberStrList])
if sorted([int(x) for x in numberStrList]) == [int(x) for x in numberStrList]:
    print("yes")
elif d:
    print("yes")
    print("swap {} {}".format(d[0] + 1, d[1] + 1))
elif e:
    print("yes")
    print("reverse {} {}".format(e[0] + 1, e[-1] + 1))
else: print("no")