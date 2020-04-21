N = int(input())

factorial_ = 1
while 0 < N <= 100:
    factorial_ *= N
    N -= 1
print(factorial_)