import calc
num1=float(input("enter num1:"))
num2=float(input("enter num2:"))
sum=calc.add(num1,num2)
print(f"addition:{sum}")  # Output: 15
print(f"subtraction:{calc.sub(num1, num2)}")  # Output: 5
print(f"multiplication:{calc.mul(num1, num2)}")  # Output: 50
print(f"division:{calc.div(num1, num2)}")  # Output: Division by zero not allowed

