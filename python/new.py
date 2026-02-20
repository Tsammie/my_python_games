# Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.


# class NegetiveNumberError(Exception):
#     def __init__ (self, message = "This is a negative number"):
#         self.message = message
#         super().__init__(self.message)
    
# def check_positive(number):
#     if number > 0:
#         print(number,"positive Number")
#     elif number < 0:
#         raise NegetiveNumberError
# check_positive(-6)

# Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.

def safe_divide(a,b): 
    try:
        div = a/b
    except ZeroDivisionError:
        return("The divisor cannot Zero")
    except TypeError:
        return("The Charater has to str or int")
    except ValueError:
        return("The number are not convetible to float")
    else:
        return(div)
    
    

sam = safe_divide(4,0)
print(sam)