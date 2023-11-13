'''6) Create a python code that takes one integer input from the user. The program should
display bada number if the input is greater than 20. Otherwise the program should display
chota number.'''
#Solution :-
def Num_chota_or_bada():

    # Taking integer input from the user
    print("Check the integer is chota or bada")
    user_input = int(input("Enter an integer: "))

 #Checking the condition
    while True:
       if user_input > 20:
         print("bada number")
       else :
         print("chota number")
       break

Num_chota_or_bada()