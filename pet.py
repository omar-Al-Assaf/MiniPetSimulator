class Pet:
    def __init__(self, name, energy_level):
        self.name = name
        self.energy_level = energy_level

    def play_with_pet(self):
        self.energy_level -= 10
        print(f"{self.name} played and lost some energy.")