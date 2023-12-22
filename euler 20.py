factorial = 1

def sum(factorial):
    result = 0
    for m in range(1,len(factorial)): result += int(factorial[m-1:m])
    return result

for n in range(1,101): factorial *= n

print(sum(str(factorial)))
