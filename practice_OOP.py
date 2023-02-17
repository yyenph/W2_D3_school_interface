class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} eats a {food}.")

    def speak(self):
        print("I'm an animal!")


class Dog(Animal):
    is_service_animal=T
    def __init__(self, name, is_service_animal):
        super().__init__
        self.is_service_animal = is_service_animal

    def speak(self):
        if self.is_service_animal:
            print(f"{self.internal_repr_animal.name} at your service")
        else:
            print("BARK BARK!")


fido = Dog('Fido', False)
sparky = Dog('Sparky', True)