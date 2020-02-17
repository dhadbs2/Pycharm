f1, f2 = map(int, input().split())
a = f1//10 # f1의 십의 자리
b = f2//10 # f2의 십의 자리
x = f1 % 10 # f1의 일의 자리
y = f2 % 10 # f2의 일의 자리
if a >= b:
    if x < y:
        z = (abs(y - x)//5) + (abs(y - x)%5) + abs(a - b)
        print(z)
    elif x > y:
        if((x-y) ==4):
            z = 2 + abs(a - b)
            print(z)
        else:
            z = (abs(y - x) // 5) + (abs(y - x) % 5) + abs(a - b)
            print(z)
    else:
        print(abs(a-b))
elif a < b:
    if x > y:
        if (b - a) == 1:
            z = (b - a) + (abs(x - y)//5) +(abs(x - y)%5)
            print(z)
        else:
            z = ((y+10-x)//5) + ((y+10-x)%5) + (b-a-1)
            print(z)
    elif x < y:
        if(abs(x-y)==4):
            z = 2 + abs(a - b)
            print(z)
        else:
            z = ((y-x)//5) + ((y-x)%5) + (b-a)
            print(z)
    else:
        print(abs(b-a))