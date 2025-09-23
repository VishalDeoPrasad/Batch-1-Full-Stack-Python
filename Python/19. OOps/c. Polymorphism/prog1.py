class Dog:
    def speak(self):
        print("Dog Speaking!")

class Cat:
    def speak(self):
        print("Cat Speaking!")

def call_pet(obj):
    obj.speak()
    
dog_obj = Dog()
call_pet(dog_obj)

cat_obj = Cat()
call_pet(cat_obj)


