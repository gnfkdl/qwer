square = [i for i in range(2,1002)]
answer = 1

answer = [square[i] * square[i] - square[i-1] * j for i in range(1,len(square),2) for j in range(0,4)]
print(sum(answer)) 
