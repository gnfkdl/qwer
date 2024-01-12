answer = []

def digits(i):
    num = [(i // 10**j % 10)**5 for j in range(0,len(str(i)))]
    return sum(num)

for i in range(1,999999): 
    if i == digits(i): answer+= i,

print(sum(answer)-1)