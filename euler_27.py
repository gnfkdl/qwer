from math import sqrt
longest_prime_chain = answer_a = answer_b = 0
all_num = {}

def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3,round(sqrt(n))+1,2):
        if n % i == 0: return False
    return True

def prime_value(a,b):
    n = 0
    while True:
        num = (n**2) + (a*n) + b
        if num not in all_num: all_num[num] = is_prime(num)
        if all_num[num]: n+= 1 
        else: break
    return n

for prime in range(1,1000): all_num[prime] = is_prime(prime)
prime = [i for i in all_num if all_num[i] == True]

for a in range(-999,1000):
    for b in prime:
        prime_chain = prime_value(a,b)
        if longest_prime_chain < prime_chain: 
            longest_prime_chain = prime_chain
            answer_a,answer_b = a,b

print(longest_prime_chain,answer_a,answer_b)
print(answer_a*answer_b)
