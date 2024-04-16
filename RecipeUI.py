import Recipe
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QGridLayout, QApplication, QLineEdit, QPushButton, QWidget, QLineEdit, QLabel
import sys


class RecipeUI(QDialog):

    def __init__(self):
        super(RecipeUI, self).__init__()

        self._recipe_list_master = []
        for i in range(512):
            self._recipe_list_master.append(Recipe.Recipe("Recipe" + str(i), "00:11", "00:22", "BANANA"))
        self._recipe_list_search = self._recipe_list_master
        self._width = 1600
        self._height = 900

        self._search_bar = QLineEdit("Enter A Keyword To Be Searched (Please seperate differnt phrases by ',' :D)")
        self._search_bar.selectAll()
        self._search_bar.setFocus()

        self._search_button = QPushButton("Search")
        self._reset_button = QPushButton("Reset")
        self._previous_button = QPushButton("<< Previous")
        self._next_button = QPushButton("Next >>")
        self._first_button = QPushButton("First")
        self._last_button = QPushButton("Last")

        self.setup_window()
    
    def setup_window(self):
        self.setGeometry(100, 100, self._width, self._height)
        self.setWindowTitle("Recipe Viewer")

        recipe_list = []
        for i in range(8):
            recipe_list.append(self._recipe_list_search[i])

        self.layout_ui(recipe_list)

    def layout_ui(self, recipes):
        #sets grid layout
        grid = QGridLayout()

        #following code creates all the buttons and assigns 
        #them to execute the right methods
        grid.addWidget(self._search_bar, 0, 0, 1, 80)

        self._search_button.clicked.connect(self.search)
        grid.addWidget(self._search_button, 0, 80, 1, 10)

        self._reset_button.clicked.connect(self.reset)
        grid.addWidget(self._reset_button, 0, 90, 1, 10)

        self._previous_button.clicked.connect(self.previous)
        grid.addWidget(self._previous_button, 80, 70, 1, 10)

        self._first_button.clicked.connect(self.first)
        grid.addWidget(self._first_button, 80, 80, 1, 5)

        self._last_button.clicked.connect(self.last)
        grid.addWidget(self._last_button, 80, 85, 1, 5)

        self._next_button.clicked.connect(self.next)
        grid.addWidget(self._next_button, 80, 90, 1, 10)

        index = 0

        for recipe in recipes:
            if (index < 4):
                grid.addWidget(QPushButton("IMAGE"), 1, 2 + (index*25), 20, 20)
                grid.addWidget(QLabel(f"Recipe #: {self._recipe_list_master.index(recipe) + 1}"), 2, 2 + (index*25), 21, 20)
                grid.addWidget(QLabel(f"Recipe Name: {recipe.get_name()}"), 3, 2 + (index*25), 22, 20)
                grid.addWidget(QLabel(f"Prep Time: {recipe.get_prep_time()}"), 4, 2 + (index*25), 23, 20)
                grid.addWidget(QLabel(f"Cook Time: {recipe.get_cook_time()}"), 5, 2 + (index*25), 24, 20)
                grid.addWidget(QPushButton("View Recipe"), 6, 12 + (index*25), 25, 10)
            else:
                grid.addWidget(QPushButton("IMAGE"), 7, 2 + ((index-4)*25), 60, 20)
                grid.addWidget(QLabel(f"Recipe #: {self._recipe_list_master.index(recipe) + 1}"), 8, 2 + ((index-4)*25), 61, 20)
                grid.addWidget(QLabel(f"Recipe Name: {recipe.get_name()}"), 9, 2 + ((index-4)*25), 62, 20)
                grid.addWidget(QLabel(f"Prep Time: {recipe.get_prep_time()}"), 10, 2 + ((index-4)*25), 63, 20)
                grid.addWidget(QLabel(f"Cook Time: {recipe.get_cook_time()}"), 11, 2 + ((index-4)*25), 64, 20)
                grid.addWidget(QPushButton("View Recipe"), 12, 12 + ((index-4)*25), 65, 10)
            index += 1

        low_index = self._recipe_list_master.index(recipes[0]) + 1
        high_index = self._recipe_list_master.index(recipes[len(recipes)-1]) + 1

        grid.addWidget(QLabel(f"Displaying {low_index}-{high_index} of {len(self._recipe_list_search)} Recipes"), 100, 0, 1, 10)

        self.setLayout(grid)

    def search(self):
        bar_text = self._search_bar.text()

        new_recipe_list_search = []

        if (bar_text.find(',') > -1):
            bar_text = bar_text.split(',')
        else:
            bar_text = [bar_text]

        for key_word in bar_text:
            for recipe in self._recipe_list_search:
                if((recipe.get_name().find(key_word) > -1) or (recipe.get_recipe_yeild().find(key_word) > -1)):
                    new_recipe_list_search.append(recipe)

        if (len(new_recipe_list_search) == 0):
            self._recipe_list_search = self._recipe_list_master
        else:
            self._recipe_list_search = new_recipe_list_search

    def next(self):
        print("NEXT")

    def previous(self):
        print("previous")

    def first(self):
        print("first")

    def last(self):
        print("last")

    def reset(self):
        print("reset")


def main():
    app = QApplication(sys.argv)
    gui = RecipeUI()
    gui.show()
    sys.exit(app.exec_())

main()