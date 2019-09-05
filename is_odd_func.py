# Write an is_odd function that uses your is_even function to determine if a 
# number is odd. That is, do not do the calculation - call a function that
# does the calculation. Hint - you will use the NOT keyword.

import is_even_func

try:
    num = int(input("Please enter any number "))
    if not is_even_func.is_even(num):
        print(f'{num} is an odd number!')
    else:
        print(f'{num} is not an odd number!')
except ValueError:
    print(f"{num} is not a number.")