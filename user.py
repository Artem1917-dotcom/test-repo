class User:
    age = 33

    def __init__(self, name):
        print("Я создался")
        print("меня зовут ", name)
        self.username = name

    def sayName(self):
     print("Меня зовут", self.username)

    def sayAge(self):
	     print(self.age) 
            
def setAge(self, newAge):
    self.age = setAge