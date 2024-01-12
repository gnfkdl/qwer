def powers(i,j):
    if i**j in cache: return False
    cache[(i**j)] = i**j
    return True

cache = {}
answer = [i*j for i in range(2,101) for j in range(2,101) if powers(i,j)]

print(len(answer))
