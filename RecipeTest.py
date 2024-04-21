from recipe import Recipe
import sys
from RecipeProcessor import RecipeProcessor
from RecipeDetails import DetailWindow
from PyQt5.QtWidgets import QApplication

recipeLoader = RecipeProcessor
recipeLoader.load__recipes("recipes.json")

recipeList = recipeLoader.get__recipes()





app = QApplication(sys.argv)
detail = DetailWindow(recipeList, 26)
detail.show()
sys.exit(app.exec_())