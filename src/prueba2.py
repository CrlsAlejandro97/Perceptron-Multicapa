import copy
l=[[1,3],3,2,3,4]

m=[]

m=copy.deepcopy(l)
m[0].append(4)
print(m)
print(l)