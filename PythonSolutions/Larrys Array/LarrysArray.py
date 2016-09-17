import copy

t = int(input())

for z in range(t):
    input()
    realList = [int(n) for n in input().split()]
    sortedList = copy.copy(realList)
    sortedList.sort()
    listLen = len(sortedList)
    for i in range(listLen - 2):
        if realList[i] == sortedList[i]:
            continue
        myInd = realList.index(sortedList[i])
        while myInd > i:
            if myInd == listLen - 1:
                temp = realList[myInd - 2]
                realList[myInd - 2] = realList[myInd - 1]
                realList[myInd - 1] = realList[myInd]
                realList[myInd] = temp
            else:
                temp = realList[myInd - 1]
                realList[myInd - 1] = realList[myInd]
                realList[myInd] = realList[myInd + 1]
                realList[myInd + 1] = temp
            myInd -= 1
    if realList[listLen - 1] == sortedList[listLen - 1]:
        print("YES")
    else:
        print("NO")