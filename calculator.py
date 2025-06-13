# simple calculator using ladder statements

operator = input("Enter an Operator(+,-,*,/):")
num1 = int(input("Enter Fist Number : "))
num2 = int(input("Enter Second Number : "))

# perform for calculation

if operator =='+':
 result = num1 + num2
 print(f"sum of {num1} + {num2} {result}")
elif operator =='-':
 result = num1 - num2
 print(f"sum of {num1} - {num2} {result}")
elif operator =='*':
  result = num1 * num2
  print(f"sum of {num1} * {num2} {result}")
elif operator =='/':
  result = num1 / num2
  print(f"sum of {num1} / {num2} {result}")
else:
  print(f" This operater is not found ")
