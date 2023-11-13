'''1) Create a python function that takes one argument as input and display in the format -
You have submitted x as input [x being the input given by user]'''
#Solution :-
def printAge(input_age):

    print(f'You have submitted {input_age} as input')

# "Age" is input that i take from user
user_age = input("Enter your current age :- ")

printAge(user_age)