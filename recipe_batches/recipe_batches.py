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
  #   keep track of ingredient amt
  #     ingredient_amt = 0
  #    keep track of recipe amt
  #     recipe_amt = 0
  #   keep track of number of batches available
    batches = 0
  #  batch = ingredients // recipe
  #   If the length of the recipe > length of ingredients return 0
  # if len(recipe) > len(ingredients):
  #     return 0
  # else:
  #     for key in ingredients:
  #         print(key, '->', ingredients[key])
  #     for key in recipe:
  #         print(key, '->', recipe[key])
  #   If values of ingredients (in the entire dictionary) are divisible by #    values of recipe continue
    for key, value in recipe.items():
        print("key", key)
        print("value", value)
        if key not in ingredients:
            return 0
        if batches > ingredients[key] // value:
            print("ingredients--key -> ", batches)
            batches = ingredients[key] // value

    return batches


recipe = {'milk': 100, 'butter': 50, 'flour': 5}
ingredients = {'milk': 132, 'butter': 48, 'flour': 51}

recipe_batches(recipe, ingredients)

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
