equal_divisor = 0

def num_divisor(num):    
    cache_1 = 0
    for i in range(1,round(num/2)+1):
        if num % i == 0: cache_1 += i

    if num == cache_1: return 0
    return cache_1

for num in range(2,10001):
    if num == num_divisor(num_divisor(num)): equal_divisor += num

print(equal_divisor)