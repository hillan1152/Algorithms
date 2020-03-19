#!/usr/bin/python

import math
# UNDERSTAND
#   Take in a DICTIONARY of a RECIPE and AVAILABLE INGREDIENTS
#     Includes key - values: name - amount
#   RECIPE DICTIONARY:
#     amount = amt of each ingredient needed for the recipe
#   INGREDIENTS DICTIONARY:
#     amount = amt of the ingredient available to you
#   GOAL/NEED: Output max number of WHOLE BATCHES
#      2nd Dictionary represents ingredients dictionary.


def recipe_batches(recipe, ingredients):
    # PLAN
    #   keep track of number of batches available
    # recipe_amt =
    #   keep track of ingredient amt
    #   keep track of recipe amt
    #
    #   If values of ingredients (in the entire dictionary) are divisible by #    values of recipe continue
    #
    pass


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
