Fibonacci = [1,1]
answer = n = 0

def get_Fibonacci(n):
    Fibonacci.append(Fibonacci[n] + Fibonacci[n+1])
    return Fibonacci


while len(str(Fibonacci[n+1])) < 1000:
    get_Fibonacci(n)
    n += 1

print(n+2)