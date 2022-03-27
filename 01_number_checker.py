# Checks the number is more than a given input value

def num_check (question):
    valid = False
    while not valid:

        error = "Please enter an integer {}".format
        error_2 = ""

        try:
            
            # ask user to enter number
            response = int(input(question))

            # checks number is more than 1
            if response >= 1:
                return response
            
            # output error if input is invalid
            else:
                print(error)
                print()
        
        except ValueError:
            print(error_2)

keep_going = ""
while keep_going == "":
    
    print()
    # ask user for integer (must be more than (or equal to) 1 and less than (or equal to) 200)
    var_integer = num_check("Enter an integer: ")
    print()

