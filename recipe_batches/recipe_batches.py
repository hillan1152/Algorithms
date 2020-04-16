#!/usr/bin/python

import math
# UNDERSTAND
# Param: Recipe
#     has a dictionary of exact number of ingredients
# Param: ingredients
#     has a dictionary of number of ingredients you have

# GOAL: output maximum number of whole batches using the ingredients available

# PLAN: if keys match, continue

recipe = {'milk': 100, 'butter': 50, 'flour': 5}
ingredients = {'milk': 132, 'butter': 100, 'flour': 51, 'water': 50}


def recipe_batches(recipe, ingredients):
    total_batches = 0
    while True:
        if recipe.keys() <= ingredients.keys():
            for i in ingredients:
                if ingredients[i] >= recipe[i]:
                    ingredients[i] -= recipe[i]
                else:
                    return total_batches
            total_batches += 1
        else:
            return total_batches


print(recipe_batches(recipe, ingredients))


length = len(recipe)

print('\n Length of Recipe --> ', length, '\n')
# print('\n Messing With Lengths --> ', recipe[length], '\n')
print('\n Testing Keys --> ', recipe.keys(), '\n')
# Gets number of ingredients from a dictionary
print('\n Testing Get --> ', recipe.get('milk'), '\n')
print('\n Testing Items --> ', recipe.items(), '\n')
# print('\n Testing FromKeys --> ', recipe.fromkeys(recipe, 100), '\n')


if recipe.keys() == ingredients.keys():
    print('YEP')
else:
    print('NOPE')

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
