st={}
print(type(st))
set={1,2,2,3}
print(type(set))
set1={2,3,4,5}
set.update(set1)
print(set)
unionset=set.union(set1)
intersectionset=set.intersection(set1)
diff=set.difference(set1)
print(unionset,intersectionset,diff)