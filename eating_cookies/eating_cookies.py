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


#   CLASS NOTES
#       Looking for permuations, probably exponential 3^n?
def eating_cookies(n, cache=None):
    if cache is None:
        cache = {}
    # base cases
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif cache and cache[n]:
        return cache[n]
    else:
        cache[n] = eating_cookies(
            n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)

    return cache[n]


print(eating_cookies(40, {}))
# def eating_cookies(n, cache=None):
#     # POSSIBLE WAYS = 0
#     # TAKE N
#     # IF 0 RETURN ZERO
#     if n < 0:
#         return n
#     if n == 0:
#         return 1
#     else:
#         return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
