import sys
import time
# this function implements loading bar. while all recipe objects are "created" with recipe.__init__
# the time-consuming initialization logic is moved to a seperate recipe.initialize function
# which prevents doing unnecessary work for unused objects (and allows progress bar to be useful)
# this function is just a prototype; TODO: implement correctly
def initialize_all(recipe_array, bar_length = 50):
    progress_max = len(recipe_array)
    for i, r in enumerate(recipe_array):
        percent = i/progress_max
        left_half= '#' * int(percent * bar_length)
        right_half = ' ' * int((1-percent)*bar_length)
        sys.stdout.flush()
        sys.stdout.write("\r\033[K"+left_half+right_half)
        r.initialize()
    print()
from recipe import *
class RecipeBuffer: #FINAlish implementation
    def __init__(self,data, buffer_size):
        self.data = data
        self.buffer_size = buffer_size
        self.buffer_index = 0
        # initialize_all(self.data)    SHOULD THIS GO HERE OR BELOW???
    def current(self):
        output = []
        for i in range(self.buffer_size):
            index = self.buffer_index+i
            if(index>=len(self.data)):
                continue
            output.append(self.data[index])
        initialize_all(output)       # SHOULD THIS GO HERE OR ABOVE???
        return output
    def next(self):
        new_index = self.buffer_index+self.buffer_size
        if(new_index>=len(self.data)):
            raise IndexError("RecipeBuffer has no next")
        self.buffer_index = new_index
        return self.get_current()
    def previous(self):
        new_index = self.buffer_index - self.buffer_size
        if(new_index<0):
            raise IndexError("RecipeBuffer has no previous")
        self.buffer_index = new_index
        return self.get_current()
    def first(self):
        self.buffer_index = 0
        return self.get_current()
    def last(self):
        self.buffer_index = len(self.data) - (len(self.data)%self.buffer_size)
        return self.get_current()
    def has_next(self):
        return((self.buffer_index+self.buffer_size) < len(self.data))
    def has_previous(self):
        return((self.buffer_index-self.buffer_size) >= 0)