for i in range(10):
    print(i)
    if i == 5:
        break  #break force the program to exit the loop

else:
    print('this is inside else of for') #because of break this line wont be going to execute. because for loop isnt executed fully