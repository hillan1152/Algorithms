#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
# UNDERSTAND
#   CAN EAT 0, 1, 2, OR 3
#   NEED TO COUNT NUMBER OF **POSSIBLE** WAYS TO COUNT
#   CACHE USED TO KEEP TRACK OF REPITIION
#   MATH TYPES:
#     IT CAN BE DIVISIBLE BY 3
#     CAN HAVE THE REMAINDER BE DIVIDED OTHER NUMBERS


def eating_cookies(n, cache=None):
    # POSSIBLE WAYS = 0
    # TAKE N
    total_cookies = n
    ways = 0
    # IF 0 RETURN ZERO
    if n <= 0:
        pass
    # IF N IS DIVISIBLE BY 1
    if n % 1 == 0:
        # ADD 1 WAYS
        ways += 1
    # IF N IS DIVISIBLE BY 2
    if n % 2 == 0:
        # ADD 1 WAYS
        ways += 1
    if n % 3 == 0:
        ways += 1
    #   IF REMAINDER/3
    #     ADD 1 WAYS
    #   IF N IS DIVISIBLE BY 1
    #   ADD 1 WAYS
    # IF N IS DIVISIBLE BY 3
    #   ADD 1 WAYS
    #   IF REMAINDER/3
    #     ADD 1 WAYS
    # Return ways

    return ways


print(eating_cookies(6))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
