n, m = map(int, input().split())
s = [list(input()) for i in range(n)]
ans = 0

def star(i, j, c):
    s[i][j]=c
    for h in range(1,n):
      if i+h<n and i-h>=0 and j+h<m and j-h>=0 and s[i+h][j]=="G" and s[i-h][j]=="G" and s[i][j+h]=="G" and s[i][j-h]=="G":
        s[i+h][j]=s[i-h][j]=s[i][j+h]=s[i][j-h]=c
      else: break  

def calc():
    t1=t2=0 
    for i in range(n):
      for j in range(m):
        if s[i][j] == "B": continue
        if s[i][j] == "1": t1 += 1
        if s[i][j] == "2": t2 += 1
        s[i][j] = "G"
    return t1*t2
    
def check(i, j, ii, jj):
    if s[i][j] != "G" or s[ii][jj] != "G" : return 0
    star(i, j, '1'); star(ii, jj, '2'); c1 = calc()
    star(ii, jj, '1'); star(i, j, '2'); c2 = calc()
    return c1 if c1>c2 else c2

for k1 in range(n*m):
  for k2 in range(k1+1,n*m):
    ans = max(ans, check(k1//m,k1%m,k2//m,k2%m))

print(ans)