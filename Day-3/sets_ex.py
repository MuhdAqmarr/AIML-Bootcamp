# print("Sets in Python")
# set_one={'laptop','mobile','ipad','tablet','desktop','laptop','ipad'}
# print('Number of items are: ',len(set_one))
# for item in set_one:
#     print(item, end=" ")

# #clear(): Removes all the elements from the set
# set_one.clear()
# print('\nAfter clear Number of items are: ',len(set_one))
# for item in set_one:
#     print(item, end=" ")


# set_one={'laptop','mobile','ipad','tablet','desktop'}
# print('Number of items are: ',len(set_one))
# for item in set_one:
#     print(item, end=" ")
# #remove(): Removes the specified element from the set
# set_one.remove('ipad')
# print('\nAfter remove Number of items are: ',len(set_one))
# for item in set_one:
#     print(item, end=" ")


#union, intersection, difference
set_one={100,200,300,500,700,900,150}
set_two={100,400,700,1000,1300}

#union
#s1.union(s2): Returns a set that contains all items from both sets, excluding duplicates.
# print(f'set_one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)} items')
# print(set_two)
# unionset=set_one.union(set_two)
# print(f'Union of set_one and set_two contains: {len(unionset)} following items')

# print(unionset)


#intersection
#s1.intersection(s2): Returns a set that contains only the items that are present in both sets.
print(f'set_one contains: {len(set_one)} items')
print(set_one)
print(f'set_two contains: {len(set_two)} items')
print(set_two)
newset=set_one.intersection(set_two)
print(f'Intersection of set_one and set_two contains: {len(newset)} following items')

print(newset)


