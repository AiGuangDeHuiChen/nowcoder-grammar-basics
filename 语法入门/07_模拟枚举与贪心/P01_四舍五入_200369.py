n,t=map(int,input().split())
s=input()
if '.' not in s:
    print(s)
    exit()
pi,pf=s.split('.')
pi=int(pi)
c=0
flag=False
while t!=0:
    for i in range(len(pf)):
        if pf[0]>='5':
            pi+=1
            flag=True
            break
        elif pf[i]>='5':
            pf=str(int(pf[:i])+1)
            break
    t-=1
    if flag:
        break
if flag:
    print(pi)
else:
    print(str(pi)+'.'+pf)