from recipe import Recipe
from json import loads

class RecipeProcessor:
    global recipes
    recipes = []
    def load__recipes(json_file):
        with open(json_file, 'r', encoding = 'utf-8') as file:
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

    def get__recipes():
        return recipes