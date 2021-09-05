name = input('Student name: ')
family = input('Student Family: ')
score1  = float(input('Enter 1st score'))
score2 = float(input('Enter 2nd score'))
score3  = float(input('Enter 3rd score'))
average = score3+score2+score1
average = average/3
print (name +" "+family+' is:')
if average < 12:
    print('fail')
if average >= 12 and average < 17:

    print('pass')
if average >=17 :
    print('great')