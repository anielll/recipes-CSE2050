import sys
from recipe import Recipe
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton, QWidget, QLabel, QListWidget
from RecipeProcessor import RecipeProcessor

class DetailWindow(QDialog):

    def __init__(self, recipe, index):
        super(DetailWindow, self).__init__()
        self.recipe = recipe
        self.index = index
        self.title = recipe.get_name()
        self._width = 400
        self._height = 600
        self.setup_window()
    def setup_window(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(100,100, self._width, 100)
        self.setWindowTitle(self.title)
        self.layout_detail(self.recipe)
    
    def layout_detail(self, recipe):
        image_label = QLabel()
        image_pix = QPixmap(recipe.get_image())
        if(image_pix.isNull()): # invalid file
            self.grid.addWidget(QPushButton("IMAGE NOT FOUND"), 0, 0)
        else:
            image_pix = image_pix.scaled(400,300, Qt.KeepAspectRatio)
            image_label.setPixmap(image_pix)
            self.grid.addWidget(image_label, 0, 0, 1, -1)
        self.grid.addWidget(QLabel("Recipe #:"), 1, 0, Qt.AlignTop)
        self.grid.addWidget(QLabel("Recipe Name:"), 2, 0, Qt.AlignTop)
        self.grid.addWidget(QLabel("Prep Time:"), 3, 0, Qt.AlignTop)
        self.grid.addWidget(QLabel("Cook Time:"), 4, 0, Qt.AlignTop)
        self.grid.addWidget(QLabel("Description:"), 5, 0, Qt.AlignTop)
        self.grid.addWidget(QLabel("Ingredients:"), 6, 0, Qt.AlignTop)
        self.grid.addWidget(QLabel("Recipe Yield:"), 7, 0, Qt.AlignTop)
        self.grid.addWidget(QLabel(f"{self.index + 1}"), 1, 1)
        self.grid.addWidget(QLabel(self.recipe.get_name()), 2, 1)
        self.grid.addWidget(QLabel(self.recipe.get_prep_time()), 3, 1)
        self.grid.addWidget(QLabel(self.recipe.get_cook_time()), 4, 1)
        self.descriptionLabel = QLabel(self.recipe.get_description())
        self.descriptionLabel.setWordWrap(True)
        self.grid.addWidget(self.descriptionLabel, 5, 1)
        self.ingredientList = ""
        for x in self.recipe.get_ingredients():
            self.ingredientList = self.ingredientList + x + "\n"
        self.ingredientLabel = QLabel(self.ingredientList)
        self.ingredientLabel.setWordWrap(True)
        self.grid.addWidget(self.ingredientLabel, 6, 1)
        self.grid.addWidget(QLabel(self.recipe.get_recipe_yield()), 7, 1)