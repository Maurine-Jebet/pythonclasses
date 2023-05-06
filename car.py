class Car:
    def __init__(self,make,color,model):
        self.make = make
        self.color=color
        self.model=model
    def show_description(self):
        return f"This is a {self.color},{self.make}"
    def change_colour(self):
        return self.color
    def show_make(self):
        return f"This type {self.make} is more preferable"