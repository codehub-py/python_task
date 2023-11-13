'''5) Create a python code that takes an input from the user. The code should display the data
given input to the user in the format - You have submitted a int value [int would be
replaced by the datatype]'''
#Solution :-

def Check_datatype(user_input):
    while True:
        if user_input.isdigit():#"isdigit()" is the method which return "True" when the input is "digit(0-9)"
            print("You have submitted int value")#Here we print our statement in the place of "True"

            '''In the following condition we use "isdigit()" but this function only work when input does not contence "."
             But in case if user input float value we use "replace()" in this we remove "."'''
        elif user_input.replace(".","").isdigit():
            print("You have submitted float value")

        else:
            print("You have submitted str value")
        break
#Taking input from user
print("Check your input datatype")
user_input = input("Enter input:- ")

Check_datatype(user_input)


