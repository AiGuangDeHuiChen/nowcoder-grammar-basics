L,M=map(int,input().split())
a=[False]*(L+1)
for i in range(M):
    l,r=map(int,input().split())
    for j in range(l,r+1):
        a[j]=True
         
print(a.count(False))