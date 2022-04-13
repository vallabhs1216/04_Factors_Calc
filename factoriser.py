import math

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

#  ******* MAIN ROUTINE GOES HERE *******

# for testing factors. factors = get_factors(x). (x) is changeable 
factors = get_factors(4)
print(factors)

