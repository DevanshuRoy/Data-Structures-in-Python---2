s={4,9,1,0,2,3,2} 
#element cannot be repeated
print(s)
s.add(-4)
print(s)

s2={4,9,1,0,8}
print(s2)
print(s.difference(s2))
print(s.symmetric_difference(s2))
print(s.intersection(s2))
print(s.union(s2))