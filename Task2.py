'''2) Create a python function that takes one argument as input. The input argument must be
an integer (ensure this using python). The function should display a square of input
integer to the user.'''
#Solution:-
def integer_square(input_Num):

    # "user_input**2" formula use for  square
    print(f'Square of input valu is :- {user_input ** 2} ')

# take integer valu from user
print("To get square of number  ")
user_input= int(input("Enter the number (only integer):-  "))

integer_square(user_input)
