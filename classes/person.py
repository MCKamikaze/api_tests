from utils import utils

class Person:
    
    def __init__(self, name : str = None, age : int = None, gender : str = None, nationality : str= None) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality

    def generate_name(self):
        self.name = utils.generate_name()

    def generate_age(self):
        self.age = utils.generate_age(self.name)

    def generate_gender(self):
        self.gender = utils.generate_gender(self.name)

    def generate_nationality(self):
        self.nationality = utils.generate_nationality(self.name)

    def generate_all(self):
        self.generate_name()
        self.generate_age()
        self.generate_gender()
        self.generate_nationality()
        