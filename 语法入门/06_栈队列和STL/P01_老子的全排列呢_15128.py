import itertools 
a=list(range(1,9))
res=itertools.permutations(a)
for i in res:
    print(" ".join(map(str,i)))