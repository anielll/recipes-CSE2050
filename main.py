import sys
from recipe_ui import RecipeUI
from PyQt5.QtWidgets import QApplication
from recipe_processor import RecipeProcessor
def main():
    RecipeLoader = RecipeProcessor
    RecipeLoader.load__recipes('recipes.json')
    master_list = RecipeLoader.get__recipes()
    app = QApplication(sys.argv)
    gui = RecipeUI(master_list)
    gui.show()
    sys.exit(app.exec_())

main()