import sys
from RecipeUI import RecipeUI
from PyQt5.QtWidgets import QApplication
from recipe import Recipe
from RecipeProcessor import RecipeProcessor
from json import loads
def main():
    RecipeLoader = RecipeProcessor
    RecipeLoader.load__recipes
    master_list = RecipeLoader.get__recipes
    app = QApplication(sys.argv)
    gui = RecipeUI(master_list)
    gui.show()
    sys.exit(app.exec_())

main()