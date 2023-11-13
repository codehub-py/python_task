'''3) Create a python function that takes one argument as input. The input argument must be
an integer (ensure this using python). The function should display a square & cube of
input integer to the user.'''
#Solution :-
def integer_square_cube():
      #take integer valu from user and save it in variable "x"
      print("To get square & cude of number  ")
      x = int(input("Enter the number (only integer):-  "))

      #"x**2" formula use for  square
      print(f'Square :- {x**2}')

      #"x**3" formula use for Cube
      print(f'Cube :- {x**3}')

integer_square_cube()
