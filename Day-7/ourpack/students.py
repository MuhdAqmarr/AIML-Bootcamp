class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    
    def print_info(self):
        print(f"ID: {self.id}, Name: {self.name}")