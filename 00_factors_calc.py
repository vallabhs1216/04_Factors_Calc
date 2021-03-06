# Funtions go here
import math

# Puts a series of symbols at the start and end of text
def statement_generator(text, decoration):

    # Makes a 5 character string
    ends = decoration * 5

    # adds decoration to the statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print

    return ""

# Displays instructions
def instructions():

    statement_generator("Instructions / Information", "=")
    print("Please choose a facotr between 1 and 200 ")
    print()
    print("This programs assumes the factors are whole numbers. ")
    print()
    print("Press <enter> at the end of each calculation or any key to quit. ")
    print()
    return 

    
# checks input is a number more than a givevn value
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

# gets factors, returns a sorted list
# gets factors, returns a sorted list
def get_factors(to_factor):
    if to_factor == 1:
        return [1]

    # use (math.) for calculations for ceil of (x) and for square root
    my_list = []
    num_sqrt = math.ceil(math.sqrt(to_factor))

    # +1 for expanding range
    for num in range(1, num_sqrt + 1):
        if to_factor % num == 0:

            # find factor by division, get whole number only 
            # (we know there is no remainder as it's a factor) 
            a_factor = to_factor // num

            my_list.append(a_factor)
            my_list.append(num)


    
    my_list.sort()

    # Unique factor stored here
    my_list = list(set(my_list))
    return my_list



# 2 factors as prime numbers only have 2
def prime(factors):
    return len(factors) == 2

# odd amount of factors in perfect squares
def perfect_squares(factors):
    return len(factors) % 2 != 0




# Main routine goes here

# Heading
statement_generator("Factors Calculator", "-")


# Displat instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue ")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask a user fo number to be factored
    var_to_factor = num_check("Enter an integer: ", low=1, high=200)

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY! It only has one factor. Itself :)"

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    # output factors and comment

    # Generate heading...
    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "Factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
print()
