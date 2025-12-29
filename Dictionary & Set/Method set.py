# set methods 

#set.add (add in element)
collection = set()
collection.add(1)
collection.add(52)
collection.add("Mr.karan thakur")

print(collection)

# set.remove 
set = {1,2,3,5,6}
set.remove(2)
print(set)

# set.clear()
set = {1,2,3,5,6}
set.clear()

print(set)

# set Methods (union)
set1 = {1,2,3,4,5,6}
set2 = {2,6,5,8,9,10}
print(set1.union(set2))


# set methods (intersection)
set1 = {1,2,3,4,5,6}
set2 = {2,6,5,8,9,10}
print(set1.intersection(set2))
