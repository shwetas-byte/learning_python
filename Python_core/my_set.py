# s={10,20,30,'python','java'}
# print(s)
# print(type(s))
# print(id(s))
# print(len(s))
# print(max(s))
# print(min(s))
# print(sum(s))

# methods for 2 or more set
# 1 to 4 new-set-created
# 1.union()
# s={1,2,3,4,5}
# s2={4,5,6,7,8}
# s3={7,8,9,10}
# print(s.union(s2.union(s3)))


# 2,intersection()
# s={1,2,3,4,5}
# s2={4,5,6,7,8}
# print(s.intersection(s2))


# 3.difference()
# s={1,2,3,4,5}
# s2={4,5,6,7,8}
# print(s.difference(s2))


# 4.symmetric difference()--both common digit removed and new set return with uncommon elements
# s={1,2,3,4,5}
# s2={4,5,6,7,8}
# print(s.symmetric_difference(s2))



# 5 to 7 old -set-update
# 5.intersection_update()
# s={1,2,3,4,5}
# s2={4,5,6,7,8}
# s.intersection_update(s2) #koi value return nahi krta hai
# print(s)


# 6.difference_update()
# s={1,2,3,4,5}
# s2={4,5,6,7,8}
# s.difference_update(s2)
# print(s)


# 7.symetric_difference_update()
# s={1,2,3,4,5}
# s2={4,5,6,7,8}
# s.symmetric_difference_update(s2)
# print(s)

# 8 to 9 boolean
# 8.issubset()
# s={1,2,3,4,5}
# s2={4,5}
# print(s2.issubset(s))

# 9.issuperset()
# s={1,2,3,4,5,6,7,8}
# s2={4,5,6,7,8}
# print(s.issuperset(s2))
# print(s)

# 10.disjoint()
# s={1,2,3,4,5,6,7,8}
# s2={4,5,6,7}
# print(s.isdisjoint(s2))

# methods work on single set--only immutable data can add in set

# 1.add()
# s={10,20,'python','java'}
# print(s.add(eval(input("Enter any element:"))))
# print(s)

# 2.update()-immutabole elements alg alg krke update krega jaise tuple me 3 element diye h toh 3 new element add krega naki pura tuple jbki add me sirf ek puri tuple ya string add hogi
# s={10,20,'python','java'}
# print(s.update(eval(input("Enter any element:"))))
# print(s)

# 3.remove()--agr vo element nahi rha toh error de dega
# s={10,20,'python','java'}
# print(s.remove(eval(input("Enter any element:"))))
# print(s)
# print(s.remove(eval(input("Enter any element:"))))
# print(s)


# 4.discard()--agr vo elemnt nahi rha toh age bd jayega or rha toh remove kr dega
# s={10,20,'python','java'}
# print(s.discard(eval(input("Enter any element:"))))
# print(s)
# print(s.discard(eval(input("Enter any element:"))))
# print(s)


# 5.pop()
# s={10,20,'python','java'}
# print(s.pop())
# print(s)

# 6.clear()--o/p set() curly braces isliye nahi kyuki {} empty curly braces dict denote krta  hai
# s={10,20,'python','java'}
# print(s.clear())
# print(s)

# 7.copy()
# s={10,20,'python','java'}
# s1=s.copy()
# print(s,s1)
# print(id(s),id(s1))