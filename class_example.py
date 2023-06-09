# # Create new class animal. All animals here will have a sound they make and a food they eat
# class Animal:
#     def __init__(self, food, sound):
#         self.food = food
#         self.sound = sound
#
#
# # Create new class dog that inherits from Animal
# # We add the breed attribute to this class
# class Dog(Animal):
#     def __init__(self, food, sound, breed):
#         super().__init__(food, sound)
#         self.breed = breed
#
#
# # Create new class cat that inherits from animal
# # We add the personality attribute
# class Cat(Animal):
#     def __init__(self, food, sound, personality):
#         super().__init__(food, sound)
#         self.personality = personality
#
#
# # Here we create an object mr_whiskers from the cat class and pass in the attributes for food, sound and
# # personality
# # We then print out his attributes
# mr_whiskers = Cat("Meat", "Meow", "Mean")
# print(f"Mr. Whiskers is {mr_whiskers.personality}. \nHe only eats {mr_whiskers.food}.\n"
#       f"At the most inconvenient times you can hear him {mr_whiskers.sound}.")
#


# Init Game class. Create attributes and a method to print out its details
class Game:
    def __init__(self, name, copies_sold, platform):
        self.name = name
        self.copies_sold = copies_sold
        self.platform = platform

    def msg(self):
        print(f"\nThe game {self.name} has sold {self.copies_sold} copies on the {self.platform}.\n")


# Init Rpg class, give it unique attributes and redefine how its msg method works.
class Rpg(Game):
    def __init__(self, name, copies_sold, platform, genre, game_length):
        super().__init__(name, copies_sold, platform)
        self.genre = genre
        self.game_length = game_length

    def msg(self):
        print(f"The game {self.name} has sold {self.copies_sold} copies on the {self.platform}.\n"
              f"It is in the {self.genre} genre and takes {self.game_length} hours to beat.\n")


# Init Fps class, give it unique attributes and redefine how its msg method works.
class Fps(Game):
    def __init__(self, name, copies_sold, platform, frame_rate, players):
        super().__init__(name, copies_sold, platform)
        self.frame_rate = frame_rate
        self.players = players

    def msg(self):
        print(f"The game {self.name} has {self.players} active players and can run up to {self.frame_rate} \n"
              f"frames per second.")


# Create object game from Game class
game = Game("Unknown", "Unknown", "Xbox")
# Call game msg method
game.msg()

# Create object rpg from Rpg class which is a child of Game class
rpg = Rpg('Skyrim', '30,000,000', "PC", "RPG", "180")
# Call game msg method
rpg.msg()

# Create object fps from Fps class which is a child of Game class
fps = Fps("Call of Duty", "30,000,000", "Cross platform", "120", "300,000")
# Call fps msg method
fps.msg()
