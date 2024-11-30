class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type  # 'cat' или 'dog'
        self.hunger = 50  # 0 - сыт, 100 - голоден
        self.energy = 50  # 0 - устал, 100 - полон сил
        self.happiness = 50  # 0 - грустен, 100 - счастлив

    def eat(self, food_amount):
        self.hunger -= food_amount
        if self.hunger < 0:
            self.hunger = 0
        self.happiness += 5
        print(f"{self.name} поел(а). Голод: {self.hunger}, Счастье: {self.happiness}")

    def sleep(self, hours):
        self.energy += hours * 10
        if self.energy > 100:
            self.energy = 100
        self.hunger += 10
        print(f"{self.name} поспал(а). Энергия: {self.energy}, Голод: {self.hunger}")

    def play(self):
        if self.energy > 20:
            self.energy -= 20
            self.happiness += 20
            print(f"{self.name} поиграл(а). Энергия: {self.energy}, Счастье: {self.happiness}")
        else:
            print(f"{self.name} слишком устал(а) для игры.")

    def mood(self):
        if self.happiness > 70:
            print(f"{self.name} счастлив(а)!")
        elif self.happiness > 40:
            print(f"{self.name} чувствует себя нормально.")
        else:
            print(f"{self.name} грустит.")

    def status(self):
        print(f"Имя: {self.name}, Вид: {self.animal_type}")
        print(f"Голод: {self.hunger}, Энергия: {self.energy}, Счастье: {self.happiness}")


# Пример использования
my_pet = Pet("Барсик", "cat")
my_pet.status()
my_pet.eat(20)
my_pet.play()
my_pet.sleep(2)
my_pet.mood()
