<<<<<<< HEAD
try:
    value = int(input('Enter an int: '))
    print(1/value)
except:
    print('Something went wrong')
else:
    print('Eveyrthing is perfect')
    
try:
    value = int(input('Enter an int: '))
    print(1/value)
except:
    print('Something went wrong')
else:
    print('Eveyrthing is perfect')
    

def get_inverse(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return None
    finally:
        print('I am always printed!')


print(get_inverse(5))


print(get_inverse(0))
=======
#Continue with code from 3.3

number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number"))
    # YOUDO.  use input function and int to set number2
except ValueError:
    print("An input was not correct")
else:
    print("No value error detected")
finally:
    print("Values taken care of")

try:
    # YOUDO divide number1 / number2 and set to answer
    # YOUDO  print the result of the division (aka answer with some helper text)
    pass  # YOUDO remove pass when done
except ZeroDivisionError:
    # YOUDO:  print message stating that division by zero is not possible.
    pass  # YOUDO remove pass when done
#YOUDO:  else and finally here as well.  
>>>>>>> bae7f558a6ec8d1d387f96240821bc7f64e20b98
