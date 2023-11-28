#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Nov 27, 2023
# This program reversed numbers and letters .

# Making a function named reverse_num


def reverse_num():
    # Getting the user input
    user_num_str = input("Enter a positive integer : ")
    # Catching anything else apart of a positive integer
    try:
        user_num_int = int(user_num_str)

    except ValueError:
        print("Invalid input")
        # After the try and catch it will try to reverse the user integer
    else:
        user_num_int_rev = str(user_num_int)[::-1]
        # And will display it

        print("Reversed number: {} ".format(user_num_int_rev))


def reverse_name():
    # Getting the user input
    user_name_str = input("Enter an name of something : ")
    # It will try to reverse the user string
    user_name_str_rev = user_name_str[::-1]
    # And will display it

    print("Reversed name: {} ".format(user_name_str_rev))

    # Calling both of our functions to def main


def main():
    reverse_num()
    reverse_name()
    # After resolving both of our functions it display this.

    print("Thanks for running my code")


if __name__ == "__main__":
    main()
