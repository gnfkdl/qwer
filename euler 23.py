abundant_num = []

def abundant(num):
    cache_1 = 0
    for i in range(1,round(num/2)+1):
        if num % i == 0: cache_1 += i
    return cache_1

def sum_include_num(num):
    for i in range(0,len(abundant_num)):
        for j in range(0,len(abundant_num)):
            if abundant_num[i] + abundant_num[j] > num: break
            else: sum_abundant_num[abundant_num[i] + abundant_num[j]] = False
    return sum_abundant_num


for num in range(1,28124):
    a = abundant(num)
    if a > num: 
        abundant_num += num,

sum_abundant_num = [False] + [True] * num
sum_include_num(num)

answer = [i for i in range(0,len(sum_abundant_num)) if sum_abundant_num[i] == True]

print(sum(answer))