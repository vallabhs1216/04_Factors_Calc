def num_check(question, low, high):
    valid = False
    while not valid:
        
        error_1= "Please enter a factor that is more than (or equal to) 1 and less (or equal to) 200"
        error_2= "Please enter a factor that does not have decimal part / enter a number"
                                                                         
        try:
        
            # Ask user to enter a number
            response = int(input(question))

            # Checks number is more than zero
            if response >= low and response <= high:
                return response

            # Outputs error if input is invalid
            else:
                print(error_1)
                print()
                
        except ValueError:
            print(error_2)

keep_going = ""
while keep_going == "":

    print()
    # Ask user for integer (must be more than (or equal to) 1 and less than (or equal to) 200)
    var_interger = num_check("Enter an integer: ", low=1, high=200)
    print()