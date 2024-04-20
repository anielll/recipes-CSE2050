from re import sub
from urllib import request
from PyQt5.QtGui import *
from os import path, makedirs, remove
def time_in_minutes(time):
    temp = sub(r'[^HM\d]', '', time)
    if(temp == ""):
        return None
    temp = temp.upper()
    temp = temp.split("H") 
    if(len(temp)>1):
        total_minutes = int(temp[0]) * 60
        temp.pop(0)
    else:
        total_minutes = 0
    temp = temp[0]
    if(temp==""):
        return total_minutes
    temp = temp.split("M")
    temp = int(temp[0])
    total_minutes+= temp
    return total_minutes
def minutes_in_hm(minutes):
    if(minutes is None):
        return ""
    H,M = divmod(minutes,60)
    return (f'{H:02}:{M:02}')
class Recipe:
    def __init__(self,name,description,image_url,recipe_yield,cook_time,prep_time,ingredients):
        self.name = name
        self.description = description
        self.image_url = image_url
        self.recipe_yield = recipe_yield
        self.cook_time = cook_time
        self.prep_time = prep_time
        self.ingredients = ingredients
        self.image_filename = "./images/"+image_url.split("/")[-1]
        self.image_exists = path.exists(self.image_filename)
        self.cook_time = time_in_minutes(self.cook_time)
        self.cook_time = minutes_in_hm(self.cook_time)
        self.prep_time = time_in_minutes(self.prep_time)
        self.prep_time = minutes_in_hm(self.prep_time)
        self.initialized = False
    def set_image(self,url=None):
        self.initialized = True
        if(self.image_exists):
            return 
        if(url is None):
            url = self.image_url
        try:
            image= request.urlopen(url).read()
        except Exception as e:
            return
        if not path.exists("./images"):
            makedirs("./images")
        with open(self.image_filename,'wb') as image_out:
            image_out.write(image)
        self.image_exists = True
    def get_name(self):
        return self.name
    def get_cook_time(self):
        return self.cook_time
    def get_prep_time(self):
        return self.prep_time
    def get_recipe_yield(self):
        return self.recipe_yield
    def get_image(self):
        if(self.image_filename is None):
            return None
        else:
            return self.image_filename