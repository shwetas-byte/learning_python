# map() --create objects
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[1,2,3,4]
def sum(n1,n2,n3):
    return n1+n2+n3
# res=map(sum,l1,l2,l3)
# print(res)   #returns only memory address
res=list(map(sum,l1,l2,l3))
print(res)

# print(list(res))
