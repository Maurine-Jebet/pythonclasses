# class Fruit:
#     def __init__(self,flavour,shape,size):
#         self.flavour = flavour
#         self.shape = shape
#         self.size = size
#     def eat_fruit(self):
#         return f"I prefer {self.flavour} of oranges"
#     def blend_fruit(self):
#         return f"fruits that are {self.shape} are easy to blend"
class Fruit:
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color
    def get_taste(self):
        return self.taste    