class Fruit:
    def __init__(self,flavour,shape,size):
        self.flavour = flavour
        self.shape = shape
        self.size = size
    def eat_fruit(self):
        return f"I prefer {self.flavour} of oranges"
    def blend_fruit(self):
        return f"fruits that are {self.shape} are easy to blend"