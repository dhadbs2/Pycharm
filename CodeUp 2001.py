a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
list1 = []
list2 = []
list1.append(a)
list1.append(b)
list1.append(c)
list2.append(x)
list2.append(y)
list1.sort()
list2.sort()
print(round((list1[0]+list2[0])*(1.1), 1))