s=input().strip()
a_count=0
is_good=True
for char in s:
    if char=='a':
        a_count+=1
    elif char=='b':
        a_count-=1
        if a_count<0:
            is_good=False
            break
    else:
        is_good=False
        break
if is_good and a_count==0:
    print('Good')
else:
    print('Bad')