# Chapter 12 Classes

# VOCABULARY
# object - everything in Python is an object.  String, int, float, list, bool, tuple, etc...
# instance - an object created using a class
# class - template for an object.
# attribute - a variable that belongs to a class
# method - function that belongs to a class
# constructor method -  def __init__()  automatically runs when the object is created
# inheritance
import random


class Student():
    first_name = ""
    last_name = ""
    email = ""
    def info(self):
        print(self.first_name, self.last_name, self.email)

student1 = Student()
student1.first_name = "Ada"  # change using dot notation
print(student1.first_name)
student1.last_name = "Lovelace"
student1.email = "alovelace@fwparker.org"

student1.info()

student2 = Student()
student2.email = "jdoe@fwparker.org"
student2.info()


# Monopoly player
class Player():
    def __init__(self):
        print("A new player has joined the game")
        self.money = 1500
        self.token = "Dog"
        self.space = 0
        self.property_list = []
        self.hotels = []
    def pass_go(self):
        self.money += 200
    def pay_rent(self, rent, other):
        self.money -= rent
        other.money += rent
        print(self.token, "paid", other.token, rent, "dollars.")
    def roll_dice(self):
        die1 = random.randrange(1, 7)
        die2 = random.randrange(1, 7)
        print(self.token, "rolled", die1 + die2)
        self.space += die1 + die2
        print(self.token, "moved to space", self.space)


player1 = Player()
player1.pass_go()
print(player1.money)

player2 = Player()
player2.token = "Thimble"

player2.pay_rent(17, player1)
print(player2.money)
print(player1.money)

player1.roll_dice()
player1.roll_dice()




