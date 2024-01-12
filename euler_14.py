def collatz(n):
    if n % 2 == 0: return round(n / 2)
    else: return 3 * n + 1

def loop_collatz(n):
    instan = []
    while True:
        instan+= n,
        if n in num: break
        if n == 1: break
        n = collatz(n)

    for i in range(0,len(instan)): 
        num[instan[i]] = len(instan) - i + num[n] -1
    return

num = {1:1}
for n in range(1,1000001):
    loop_collatz(n)

print(max(num, key=num.get))