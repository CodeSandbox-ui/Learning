s1 = int(input('enter your marks of first subject   '))
s2 = int(input('enter your marks of second subject  '))
s3 = int(input('enter your marks of third subject   '))

if(s1<33 or s2<33 or s3<33):
    print('you are fail becauce you have less than 33% marks on one Or more than one of your subject')

elif(s1+s2+s3)/3 <40:
    print('you are fail beacause your total marks are less than 40%')

else:
    print('Congratulations you have passed the exam')