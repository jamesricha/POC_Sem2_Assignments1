number1 = 0
number2 = 0

try:

  number = int(input("Enter a number"))
except  ValueError:
  print("message stating that an integer wasn't given")


try: 
    divide: number1 / number2 = 0
except ZeroDivisionError:
      print("message stating that division by zero is not possible.")