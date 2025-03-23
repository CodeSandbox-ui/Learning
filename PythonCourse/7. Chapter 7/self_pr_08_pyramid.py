num = int(input('enter the number '))

for i in range(num):
    print(' ' * (num-i), end='')
    print('*' * (2*i+1), end='')
    print(' ' * (num-i))


    