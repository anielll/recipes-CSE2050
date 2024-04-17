import sys
from RecipeUI import RecipeUI
from PyQt5.QtWidgets import QApplication
from recipe import Recipe
from json import loads
def parse_json(filename):
    recipes = []
    with open(filename,'r', encoding='utf-8') as file:
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
    master_list = parse_json("recipes.json")
    app = QApplication(sys.argv)
    gui = RecipeUI(master_list)
    gui.show()
    sys.exit(app.exec_())

main()