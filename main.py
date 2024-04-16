from json import loads
from recipebuffer import *
from recipe import *
def parse_json(filename):
    recipes = []
    with open(filename,'r') as file:
        data = loads(file.read())
    for recipe in data:
        name = recipe["name"]
        description = recipe["description"]
        image_url = recipe["image"]
        recipe_yield = recipe["recipeYield"]
        cook_time = recipe["cookTime"]
        prep_time = recipe["prepTime"]
        ingredients = recipe["ingredients"]
        recipes.append(Recipe(name,description,image_url,recipe_yield,cook_time,prep_time,ingredients))
    return recipes
def main():
    all_recipes = parse_json("recipes.json")
    #proper usage of RecipeBuffer regarding searches is to create a new recipe buffer each search, 
    #with all matching objects in an array passed into __init__, the array should be a unique pointer. 
    #then store the masterBuffer where and set set some global "currentBuffer" 
    #to the searchBuffer until query is reset
    buffer = RecipeBuffer(all_recipes,8)
    print(buffer.current())
main()