T=int(input())
for _ in range(T):
    n=int(input())
    m=n//2
    for i in range(n):
        d=abs(i-m)
        print(" "*d+"*"*(n-2*d))