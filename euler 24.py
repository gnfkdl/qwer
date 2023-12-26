def get_sequence_digit(num):
    n = num
    for i in range(0,len(factorial)):
        while n > factorial[i]:
            n -= factorial[i]
            sequence_digit[i] += 1
    return sequence_digit

def get_answer():
    for i in range(0, 9):
        m = answer.pop(i+int(sequence_digit[i]))
        answer.insert(i, m)

factorial = [362880, 40320, 5040, 720, 120, 24, 6, 2, 1] 
sequence_digit = [0, 0, 0, 0, 0, 0, 0, 0, 0]
answer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num = 1_000_000
get_sequence_digit(num)
get_answer()

print(answer)