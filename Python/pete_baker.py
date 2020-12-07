# Pete, the baker
# Level: 5kyu
'''
Problem Description: Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?
Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.
'''


def cakes(recipe, available):
      return int(min(available.get(k, 0)/recipe[k] for k in recipe))

# Test Cases

recipe = {"flour": 500, "sugar": 700, "eggs": 1, "apple": 2}
available = {"flour": 1800, "sugar": 2100, "eggs": 3, "milk": 200}

print(cakes(recipe, available))

#print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {
      #'sugar': 500, 'flour': 2000, 'milk': 2000}))

    #   for i in recipe:
    #     if i not in available: