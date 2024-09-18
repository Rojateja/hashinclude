#sets union and intersection
set1 = {1,2,3}
set2 = {4,5,6}
set3=set1.union(set2)
print(set3)
#union2(union and update exclude duplicate items)
set1 = {1,2,3}
set2 = {4,5,6}
set3=set1 | set2
print(set3)
#intersection (keep only duplicates)
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set3 = set1.intersection(set2)
print(set3)
#intersection(&)
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set3 = set1 & set2
print(set3)



