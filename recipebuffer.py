import sys
def initialize_all(recipe_array, bar_length = 50):
    missing_images = []
    for r in recipe_array:
        if(not r.image_exists and not r.initialized):
            missing_images.append(r)
    progress_max = len(missing_images)
    if(progress_max==0):
        return
    for i, r in enumerate(missing_images):
        percent = i/progress_max
        left_half= '#' * int(percent * bar_length)
        right_half = '-' * int((1-percent)*bar_length)
        sys.stdout.flush()
        sys.stdout.write(f'\r\033[KDownloading image {i+1:03} of {progress_max}    {left_half}{right_half}')
        r.set_image()
    error_count = 0
    for r in missing_images:
        if(not r.image_exists):
            error_count+=1
    if(error_count>0):
        print(f'\nDNS Error - Failed to Download {error_count} Images: Website Does Not Exist')
from recipe import *
class RecipeBuffer:
    def __init__(self,data, buffer_size):
        self.data = data
        self.buffer_size = buffer_size
        self.buffer_index = 0
        initialize_all(self.data)    #SHOULD THIS GO HERE OR BELOW???
    def current(self):
        output = []
        for i in range(self.buffer_size):
            index = self.buffer_index+i
            if(index>=len(self.data)):
                continue
            output.append(self.data[index])
        # initialize_all(output)       # SHOULD THIS GO HERE OR ABOVE???
        return output
    def next(self):
        new_index = self.buffer_index+self.buffer_size
        if(new_index>=len(self.data)):
            raise IndexError("RecipeBuffer has no next")
        self.buffer_index = new_index
        return self.current()
    def previous(self):
        new_index = self.buffer_index - self.buffer_size
        if(new_index<0):
            raise IndexError("RecipeBuffer has no previous")
        self.buffer_index = new_index
        return self.current()
    def first(self):
        self.buffer_index = 0
        return self.current()
    def last(self):
        self.buffer_index = len(self.data) - (len(self.data)%self.buffer_size)
        return self.current()
    def has_next(self):
        return((self.buffer_index+self.buffer_size) < len(self.data))
    def has_previous(self):
        return((self.buffer_index-self.buffer_size) >= 0)