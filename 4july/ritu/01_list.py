L1 = ["Apple","Orange","5","Akash","Rohan"]

print(L1[0])

print(L1[1])

print(L1[2])

print(L1[3])

print(L1[4])

L1[0] = "Akash" # Unlike Strings lists are mutable

print(L1[0])

print(L1[1:4])

# Different methods of list
# method 1
L1.append(1)

print(L1)
# method 2
L1.remove((L1[0]))

print(L1)

L2 =[8,5,3,9,33,65,84,]
# method 3
L2.sort()

print(L2)
# method 4
L2.reverse()

print(L2)
# method 5
L2.insert(3, 444444) # Insert 444444 such that its index in the list is 3

print(L2)
# method 6
L2.pop(3)

print(L2)

print(L2.pop(3))
# method 7
L2.remove(33)

print(L2)