#!/usr/bin/env python3
#
# Created by: Rodas Nega
# Created on: Oct 2021
# This program uses an array to find the largest number
#  from randomly generated numbers


import random


def largest_value(list_of_random_numbers):
    # this function finds the largest value

    # process
    max_value = list_of_random_numbers[0]
    for x_value in list_of_random_numbers:
        if x_value > max_value:
            max_value = x_value

    return max_value


def main():
    # this function uses an array to generate 10 random numbers
    #  from 1-100 and outputs the list

    random_generated_numbers = []

    # output
    for loop_counter in range(0, 10):
        number_in_array = random.randint(0, 100 + 1)
        random_generated_numbers.append(number_in_array)

    print("The random numbers from (1-100) are...")
    print("")
    print("{0}".format(random_generated_numbers))

    largest_number = largest_value(random_generated_numbers)

    print("\nThe largest number is {0}".format(largest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
