l,sum,r,c=[],0,int(input()),int(input())
for i in range (r):
  l.append(list(map(int,input().split())))
  print(l[i])
print(l[0][0]+l[r-1][0]+l[0][c-1]+l[r-1][c-1])
