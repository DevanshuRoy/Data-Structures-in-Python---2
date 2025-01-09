l=[3,6,1]
t=(4,9,1)
print(l, t)

#empty list and tuple
l=[]
l=list()
t=()
t=tuple()                   
print(l, t)

#list and tuple with single element
l=[10]
t=(10,)
t1=(10)
print(l, t, t1)
print(type(l), type(t), type(t1))

t=(5,91,0,2,7,3,0)

#tuple inside tuple, list inside list
t=(5,91,0,(2,7),3,0)
print(t(3)(1))

L=[[2,1,2],9,[1,0,-1],0,-4,3]
print(L[L[L[-2]][1]][1])

print(sum(t))
print(min(t))
print(max(t))

L=[0,7,1]
L[1]=100
print(L) #{7,100,2}

T=(0,7,1)
T[1]=100
print(L) #error