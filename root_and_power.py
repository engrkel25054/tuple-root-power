# Program specification
"""
Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 1 < pwr < 6
and root**pwr is equal to the integer entered by the user. If no such pair of integers exists,
it should print a message to that effect.
"""

number = int(input("Enter a number: "))
pair = ()
for root in range(1, number):
    for power in range(2, 6):
        if root ** power == number:
            pair = (root, power)
            print(f"The root number is {pair[0]}, raise to the power of {pair[1]}.")
            break

if len(pair) == 0:
    print("The number entered has no root.")