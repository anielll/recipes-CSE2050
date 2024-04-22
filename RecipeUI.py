from recipe import Recipe
from recipebuffer import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QGridLayout, QLineEdit, QPushButton, QWidget, QLineEdit, QLabel
from RecipeDetails import *

class RecipeUI(QDialog):

    def __init__(self, recipe_list_master):
        super(RecipeUI, self).__init__()
        self._detail_window = None
        self._master_buffer = RecipeBuffer(recipe_list_master,8)
        self._current_buffer = self._master_buffer
        self._width = 1600
        self._height = 900

        self._search_bar = QLineEdit("Enter A Keyword To Be Searched (Please separate different phrases by ',' :D)")
        self._search_bar.selectAll()
        self._search_bar.setFocus()

        self._search_button = QPushButton("Search")
        self._reset_button = QPushButton("Reset")
        self._previous_button = QPushButton("<< Previous")
        self._next_button = QPushButton("Next >>")
        self._first_button = QPushButton("First")
        self._last_button = QPushButton("Last")

        #following code creates all the buttons and assigns 
        #them to execute the right methods
        self._search_button.clicked.connect(self.search)
        self._reset_button.clicked.connect(self.reset)
        self._previous_button.clicked.connect(self.previous)
        self._first_button.clicked.connect(self.first)
        self._last_button.clicked.connect(self.last)
        self._next_button.clicked.connect(self.next)
        self.setup_window()
    def setup_window(self):        
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(100, 100, self._width, self._height)
        self.setWindowTitle("Recipe Viewer")
        self.layout_ui(self._master_buffer.current())

    def layout_ui(self, recipes):
        self.buttons =[]
        items = [self.grid.itemAt(i) for i in range(self.grid.count())]
        for item in items:
            self.grid.removeWidget(item.widget())
        items = [self.grid.itemAt(i) for i in range(self.grid.count())]
        
        self.grid.addWidget(self._search_bar, 0, 0, 1, 80)
        self.grid.addWidget(self._search_button, 0, 80, 1, 10)
        if(self._current_buffer!=self._master_buffer):
            self.grid.addWidget(self._reset_button, 0, 90, 1, 10)
            self._reset_button.show()
        else:
            self._reset_button.hide()
        if(self._current_buffer.has_previous()):
            self.grid.addWidget(self._first_button, 80, 80, 1, 5)
            self.grid.addWidget(self._previous_button, 80, 70, 1, 10)
            self._previous_button.show()
            self._first_button.show()
        else:
            self._previous_button.hide()
            self._first_button.hide()
        if(self._current_buffer.has_next()):
            self.grid.addWidget(self._next_button, 80, 90, 1, 10)
            self.grid.addWidget(self._last_button, 80, 85, 1, 5)
            self._next_button.show()
            self._last_button.show()
        else:
            self._next_button.hide()
            self._last_button.hide()
        for index, recipe in enumerate(recipes):
            recipe_image = recipe.get_image()
            if (index < 4):
                image_label = QLabel()
                image_pix = QPixmap(recipe_image)
                if(image_pix.isNull()): # invalid file
                    self.grid.addWidget(QPushButton("IMAGE NOT FOUND"), 1, 2 + (index*25), 10, 20)
                else:
                    image_pix = image_pix.scaled(300,300, Qt.KeepAspectRatio)
                    image_label.setPixmap(image_pix)
                    self.grid.addWidget(image_label, 1, 2 + (index*25), 10, 20)
                self.grid.addWidget(QLabel(f"Recipe #: {self._current_buffer.buffer_index+index + 1}"), 22, 2 + (index*25), 1, 20)
                recipe_name = recipe.get_name()
                if (len(recipe_name) > 40):
                    target_index = recipe_name[30:].find(" ") + 30
                    recipe_string = f"Recipe Name: {recipe.get_name()[:target_index]}" + "\n" + f"{recipe.get_name()[target_index:]}"
                    self.grid.addWidget(QLabel(recipe_string), 23, 2 + (index*25), 2, 20)
                else:
                    self.grid.addWidget(QLabel(f"Recipe Name: {recipe.get_name()}"), 23, 2 + (index*25), 2, 20)
                self.grid.addWidget(QLabel(f"Prep Time: {recipe.get_prep_time()}"), 25, 2 + (index*25), 1, 20)
                self.grid.addWidget(QLabel(f"Cook Time: {recipe.get_cook_time()}"), 26, 2 + (index*25), 1, 20)
                view_button = QPushButton("View Recipe")
                self.buttons.append(view_button)
                self.grid.addWidget(view_button, 27, 12 + (index*25), 1, 10)
            else:
                image_label = QLabel()
                image_pix = QPixmap(recipe_image)
                if(image_pix.isNull()): # invalid file
                    self.grid.addWidget(QPushButton("IMAGE NOT FOUND"), 28, 2 + ((index-4)*25), 10, 20)
                else:
                    image_pix = image_pix.scaled(300,300, Qt.KeepAspectRatio)
                    image_label.setPixmap(image_pix)
                    self.grid.addWidget(image_label, 28, 2 + ((index-4)*25), 10, 20)
                self.grid.addWidget(QLabel(f"Recipe #: {self._current_buffer.buffer_index+index + 1}"), 42, 2 + ((index-4)*25), 1, 20)
                recipe_name = recipe.get_name()
                if (len(recipe_name) > 40):
                    target_index = recipe_name[30:].find(" ") + 30
                    recipe_string = f"Recipe Name: {recipe.get_name()[:target_index]}" + "\n" + f"{recipe.get_name()[target_index:]}"
                    self.grid.addWidget(QLabel(recipe_string), 43, 2 + ((index-4)*25), 2, 20)
                else:
                    self.grid.addWidget(QLabel(f"Recipe Name: {recipe.get_name()}"), 43, 2 + ((index-4)*25), 2, 20)
                self.grid.addWidget(QLabel(f"Prep Time: {recipe.get_prep_time()}"), 45, 2 + ((index-4)*25), 1, 20)
                self.grid.addWidget(QLabel(f"Cook Time: {recipe.get_cook_time()}"), 46, 2 + ((index-4)*25), 1, 20)
                view_button = QPushButton("View Recipe")
                self.buttons.append(view_button)
                self.grid.addWidget(view_button, 47, 12 + ((index-4)*25), 1, 10)

        low_index = self._current_buffer.buffer_index + 1
        high_index = low_index + self._current_buffer.buffer_size -1
        high_index = min(high_index, len(self._master_buffer.data))

        self.grid.addWidget(QLabel(f"Displaying {low_index}-{high_index} of {len(self._current_buffer.data)} Recipes"), 100, 0, 1, 10)
        # i tried to do this in the main loop but lambda functions are not dynamic 
        self.buttons[0].clicked.connect(lambda: self.view(recipes[0],self._current_buffer.buffer_index+1))
        self.buttons[1].clicked.connect(lambda: self.view(recipes[1],self._current_buffer.buffer_index+2))
        self.buttons[2].clicked.connect(lambda: self.view(recipes[2],self._current_buffer.buffer_index+3))
        self.buttons[3].clicked.connect(lambda: self.view(recipes[3],self._current_buffer.buffer_index+4))
        self.buttons[4].clicked.connect(lambda: self.view(recipes[4],self._current_buffer.buffer_index+5))
        self.buttons[5].clicked.connect(lambda: self.view(recipes[5],self._current_buffer.buffer_index+6))
        self.buttons[6].clicked.connect(lambda: self.view(recipes[6],self._current_buffer.buffer_index+7))
        self.buttons[7].clicked.connect(lambda: self.view(recipes[7],self._current_buffer.buffer_index+8))                        
    def search(self):
        bar_text = self._search_bar.text()

        new_recipe_list_search = []

        if (bar_text.find(',') > -1):
            bar_text = bar_text.split(',')
        else:
            bar_text = [bar_text]

        for key_word in bar_text:
            for recipe in self._master_buffer.data:
                if((recipe.get_name().find(key_word) > -1) or (recipe.get_recipe_yield().find(key_word) > -1)):
                    new_recipe_list_search.append(recipe)

        if (len(new_recipe_list_search) == 0):
            self._current_buffer = self._master_buffer
        else:
            self._current_buffer = RecipeBuffer(new_recipe_list_search,8)
            self.layout_ui(self._current_buffer.current())
    def next(self):
        self.layout_ui(self._current_buffer.next())

    def previous(self):
        self.layout_ui(self._current_buffer.previous())

    def first(self):
        self.layout_ui(self._current_buffer.first())

    def last(self):
        self.layout_ui(self._current_buffer.last())

    def reset(self):
        self._current_buffer = self._master_buffer
        self.layout_ui(self._current_buffer.first())

    def view(self, recipe, index):
        self._detail_window = DetailWindow(recipe,index)
        self._detail_window.show()