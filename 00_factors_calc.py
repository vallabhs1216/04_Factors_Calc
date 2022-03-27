#


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
    var_to_factor = num_check("Number? ")

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
    keep_going = input("Press <enter> to continue or any jey to quit ")

print()
print("Thank you for using the factors calculator")