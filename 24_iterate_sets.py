#!/usr/bin/env python3
A={1,2,"rbnb",(1,5,6,9),"CDJ"}
print(A)
A.add(55)
A.update([5,6,9,8])
print(A)
A.discard("rbmb")
print(A)
A.remove(2)
print(A)
B={99,88,66,55,5,"rbnb",2}
C=A.union(B)
print(C)
