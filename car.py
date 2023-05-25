# class Car:
#     def __init__(self,make,color,model):
#         self.make = make
#         self.color=color
#         self.model=model
#     def show_description(self):
#         return f"This is a {self.color},{self.make}"
#     def change_colour(self):
#         return self.color
#     def show_make(self):
#         return f"This type {self.make} is more preferable"
    


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.distance = 0
    def get_descriptive_name(self):
        name = f"{self.year} {self.make} {self.model}"
        return name.title()
    def read_distance(self):
        return (f"This car has {self.distance} miles on it.")
    def update_distance(self, mileage):
        if mileage >= self.distance:
            self.distance = mileage
            return mileage
        else:
            return("You can't roll back an odometer!")
    def increment_distance(self, miles):
        self.distance+= miles
        return miles
nissan=Car("Vits","nissam",2006)
print(nissan.get_descriptive_name())
print(nissan.read_distance())
print(nissan.update_distance(200))
print(nissan.increment_distance(400))