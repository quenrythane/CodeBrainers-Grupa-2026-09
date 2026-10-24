def kot():
    print("miaucze")

kot()

class MyCat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("Meow ~" + self.name)


mruczek = MyCat("Mruczek", 5)
garfield = MyCat("Garfield", 40)

mruczek.show()
garfield.show()
print("mruczek", type(mruczek))
print(mruczek.age)
mruczek.age = 66
print(mruczek.age)
mruczek.speak()
print(garfield.age)

# [1, 2, 3].append(4)



