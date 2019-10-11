#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  finished = 0
  total = 0
  while finished == 0:
    for i in recipe.keys():
      if i in ingredients.keys():
        ingredients[i] = ingredients[i] - recipe[i]
        if ingredients[i] < 0:
          finished = 1
      else:
        return 0
    if finished == 0:
      total = total + 1
  return total


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))