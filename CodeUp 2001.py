list1 = []
list2 = []
for i in range(3):
    list1.append(int(input()))
for i in range(2):
    list2.append(int(input()))
list1.sort()
list2.sort()
print(round((list1[0]+list2[0])*(1.1), 1))