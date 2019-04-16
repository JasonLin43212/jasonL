#union of the sets a and b denoted a U b
# is the set of all objects that are a member of a or b or both
def union(a,b):
    return [x for x in a] + [y for y in b if y not in a]
print(union([1,2,3],[2,3,4]))

# intersection of a and b
# set of all objects that are a member of both A and B
def intersection(a,b):
    return [x for x in a if x in b]
# print(intersection([1,2,3],[2,3,4]))

# set difference  denoted by U\a
# all members of u that are not in a
# when a is a subset of u the set difference U | A is also called the complement of A and u
def difference(u,a):
    return [ x for x in u if x not in a]
# print(difference([1,2,3],[2,3,4]))

#symmetric difference of sets A and B denoted A delta B or A theta B
#elements which are in one of the sets but not in both
def symmetric(a,b):
    return [x for x in a+b if not (x in a and x in b)]
#print(symmetric([1,2,3],[2,3,4]))

#cartesian product of A and B denoted by axb is the set of all possibe ordered pairs (a,b)
# where a is a member of A and b is a member of B
def cartesian(a,b):
    return [(x,y) for x in a for y in b]
# print(cartesian(['hello',5,"bye"],[3,'lol',90]))
