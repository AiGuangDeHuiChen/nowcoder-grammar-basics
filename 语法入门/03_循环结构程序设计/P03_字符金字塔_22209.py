m=input().strip()
n=ord(m)-ord("A")+1
for i in range(1,n+1):
    line=" "*(n-i)
    for j in range(i):
        line=line+chr(ord("A")+j)
    for j in range(i-2,-1,-1):
        line=line+chr(ord("A")+j)
    print(line)