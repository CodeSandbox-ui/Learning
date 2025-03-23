from math import factorial


num = int(input('enter the numbar '))

factorial = 1

for i in range(1, num+1):
    factorial = factorial * i

print(f'the factorial of this number is {factorial}')

