a, b = map(int, input().split())
count = int(0)
count += abs(a - b) // 10
pow = abs(a - b) % 10
if pow == 1 or pow == 5:
    count += 1
elif pow == 2 or pow == 4 or pow == 6 or pow == 9:
    count += 2
elif pow == 3 or pow == 7 or pow == 8:
    count += 3
print(count)