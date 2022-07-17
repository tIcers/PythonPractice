sets = set()

sets.add(1)
sets.add(2)
print(sets)

# can i clear this

sets.clear()
print(sets)

# i will get back to you later

sets = {1,2,3,4}

sets_copy = sets.copy()
print(sets_copy)
print(sets)

sets1 = {1,2,3}
sets2 = {4,5,1}

sets1.difference_update(sets2)
print(sets1)

print(sets)

sets.discard(2)

print(sets)

# joint 

se1 = {1,2}
se2 = {1,2,4}
se3 = {5}

se1.isdisjoint(se3)
