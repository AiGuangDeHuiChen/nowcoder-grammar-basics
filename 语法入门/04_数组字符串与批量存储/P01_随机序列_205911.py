T = int(input())
for i in range(T):
    n = int(input())
    listA = list(map(int,input().split()))
    maxLi = max(listA)
    minLi = min(listA)
    sub = maxLi - minLi
    sum = 0
    for i in listA:
        sum += i
    avg = sum / n
    fangcha = 0.0
    for i in listA:
        fangcha += (i - avg) ** 2/n
    print(sub,end = " ")
    print(f"{fangcha:.3f}")