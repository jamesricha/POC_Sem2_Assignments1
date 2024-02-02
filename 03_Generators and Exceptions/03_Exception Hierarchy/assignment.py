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

try:
    number1 = int(input("Enter a number"))
    # YOUDO.  use input function and int to set number2
except ValueError:
    # print message stating that an integer wasn't given
    pass #YOUDO remove pass when done


  

