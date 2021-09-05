weight = float(input("Input weight in kg "))
height = float(input('Input height in cm '))
height = height / 100
Bmi = weight / height**2
print('your bmi is ', Bmi)