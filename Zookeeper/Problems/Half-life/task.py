N = int(input())
R = int(input())

count = 0
while N > R:
    N //= 2
    count += 1

print(count * 12)