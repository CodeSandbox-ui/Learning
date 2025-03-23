a = str(input('enter the username '))

a = (len(a))

if(a<10):
    print('entered username contain ' + str(a) + ' characters and it is acceptable')
    
else:
    print('entered usename contain 10 or more than 10 characters and it is not acceptable')