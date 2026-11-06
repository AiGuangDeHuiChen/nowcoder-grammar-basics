n=int(input())
a=list(map(int,input().split()))[:n]
if a[n-1]==0:
        print("UP")
elif a[n-1]==15:
        print("DOWN")
elif n<2:
    print(-1)
 
elif a[n-1]>a[n-2] :
        print("UP")
elif a[n-1]<a[n-2]:
        print("DOWN")
else:
        print(-1)