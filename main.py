class plant:
    def __init__(self, name, size, kind):
        self.name = name
        self.size = size
        self.kind = kind

class Apple(plant):
    def __init__(self, name, size, kind):
        super().__init__(name, size, kind)
        self.size = 3

    def details(self):
        print(f"name: {self.name} \nsize: {self.size} \nkind: {self.kind}")


class Bamboo(plant):
    def __init__(self, name, size, kind):
        super().__init__(name, size, kind)
        self.size = 10

    def details(self):
        print(f"name: {self.name} \nsize: {self.size} \nkind: {self.kind}")

class Rose(plant):
    def __init__(self, name, size, kind):
        super().__init__(name, size, kind)
        self.size = 0.5

    def details(self):
        print(f"name: {self.name} \nsize: {self.size} \nkind: {self.kind}")


apple = Apple("apple", 0, "tree")
apple.details()
print("____")
bamboo = Bamboo("bamboo", 0, "grass")
bamboo.details()
print("____")
rose = Rose("rose", 0, "flower")
rose.details()



