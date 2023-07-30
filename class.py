''' 
class Employee:
    name = "Prayas"
    marks = 34
    center = "Delhi"

def printObj(self):
    print(f"The name {self.name}")
    


Prayas = Employee()
print(Prayas.marks)
print(Prayas.center)
print(Prayas.name )
Prayas.printObj()
 ''' 

class Employee:
    def __init__(self, name, marks):
        self = name
        self.marks = marks

    def printObj(self):
        print(f"The name is {self.name}")
        print(f"The name is {self.marks}")

        @staticmethod
        def greet():
            print("Good day")

            
            Prayas = Employee("Prayas", 78)
            Prayas.printObj()
                  
