
from Classes.random_number import Random_a_number

class Seeker_game:

    def __init__(self):
        self.range_number_start = 0
        self.range_number_finish = 0

        self.number_to_find = 0
        self.number_player = 0

        self.range_number_start = int (input ("RANGE TO STAR: "))
        self.range_number_finish = int (input ("RANGE TO STAR: "))

        self.number = 0
      
    def find_a_number(self):
        self.number_player = int(input ("GUESS THE NUMBER: "))
        xx = Random_a_number()
        self.number = xx.find_a_random_number(self.range_number_start,self.range_number_finish )
        print(self.number)
        #self.number_to_find = number.find_a_random_number()
        
    def print_random_number(self):
        print (self.number_to_find)

    def guess_number(self,  number:int, guessed:int):
        if number == guessed:
            self.number_player = 0
            print ("YOU GUESSED - GOOD JOB")
        elif number > guessed:
            print ("GO UP! - YOU ARE NEAR")
        elif number < guessed:
            print ("GO DOWN! - ALMOST ALREADY")
        else:
            print ("ERROR")
