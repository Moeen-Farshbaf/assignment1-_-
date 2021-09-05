from math import factorial


while True:
    import math

    actions = ['sin','cos','sqroot','cot','tan','factorial','sum','sub','divide','multiply','expo']
    ind = 1 
    for action in actions:
        
        print(ind, '. ',action)
        ind = ind + 1
    op=int(input("Please enter the number of action from list above."))

    if op==1 or op==2 or op==3 or op == 6:
        a=float(input('Enter the number.'))

    else:
        a=float(input('Enter the first number'))
        b=float(input('Enter the second number'))
    
    


    if op ==7 :
        result=a+b
    elif op==8:
        result=a-b
    elif op==10 :
        result=a*b
    elif op ==9:
        if b==0 :
            result='can not divide by zero'
        else:
            result=a/b
    elif op == 6:
        result = math.factorial(a)
    elif op==11:
        result=a**b
    elif op==3: 
        result=math.sqrt(a)
    elif op==1:
        result=math.sin(a)
    elif op ==2:
        result=math.cos(a)
    elif op ==4:
        result=math.tan(a)
    elif op ==5:
        result=1/math.tan(a)
    else:
        result='error!operator not found'
    print(result)

    if input("done?") == 'done':
        break
