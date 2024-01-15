longest_float, longest_denominator = 0

def fraction(denominator):
    menurator = 1
    digit_of_floats = [] 

    while menurator != 0:
        if menurator in digit_of_floats:    return len(digit_of_floats) - digit_of_floats.index(menurator)

        digit_of_floats.append(menurator)
        menurator *= 10

        while menurator < denominator: 
            digit_of_floats.append(0)
            menurator *= 10

        menurator %= denominator
    return 0


for denominator in range(1,1001):
    cache = fraction(denominator)
    if longest_float < cache:   longest_float, longest_denominator = cache, denominator 

print('가장 큰 순환을 가지는 분수 값:',longest_denominator)
