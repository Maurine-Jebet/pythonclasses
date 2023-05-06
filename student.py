class Student:
   first_name="Maurine"
   last_name = "Jebet"
   age = 19
   school = "AkiraChix"
   country = "Kenya"


class Student:
    school="AkiraChix"
    def __init__(self,first_name,last_name,age,country) :
    #    attributes
       self.first_name=first_name
       self.last_name=last_name
       self.age=age
       self.country=country
       
    def greet_student(self):
        return f"hello {self.name} from {self.country} welcome to {self.school}"
    def show_fullname(self):
       return(f"{self.first_name} + "" + {self.last_name}")
    def year_of_birth(self):
       self.current_year=2023
       return self.current_year-self.age
    def show_initial(self):
       return f"{self.first_name[0]}{self.last_name[0]}"
