import re
import getpass
from dictionary import Dictionary

class Game:
    def __init__(self, word):
        self.word = word

    @classmethod
    def start(cls):
        print("Welcome to Wordle!")
        num_players = input("Enter number of players:")
        while num_players != "1" and num_players != "2":
            num_players = input("Sorry, you may only select 1 or 2.\nEnter number of players:")
        if num_players == "1":
            cls.one_player()
        elif num_players == "2":
            cls.two_player()
        cls.end()

    @classmethod
    def one_player(cls):
        #word = Dictionary("C:\\Users\\joeda\\coding\\wordle-app\\wordlist.txt").choose_word()
        word = Dictionary("https://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt").choose_word()
        word = word.upper()
        game = Game(word)
        game.play()          

    @classmethod
    def two_player(cls):
        word = getpass.getpass("\nEnter a 5 letter word:")
        while cls.check_input(word):
            word = getpass.getpass("\nEnter a 5 letter word:")
        word = word.upper()         
        game = Game(word)
        game.play()
    
    @classmethod
    def check_input(cls,input):
        if re.findall("[^a-zA-Z]", input) or len(input) != 5:
                print("Invalid input - try again.")
                return True

    def feedback(self,word,guess):
            fb = ["_","_","_","_","_",]
            wl = list(word)
            gl = list(guess)
            i = 0
            for x in wl:
                if gl[i] == wl[i]:
                    fb[i] = "!"
                elif gl[i] in wl:
                    fb[i] = "?"
                i += 1
            print(" ".join(gl) + "\n" +  " ".join(fb) + "\n")
    
    def guesses_remaining(self,i):
        g = "guesses remaining."
        if i == 4:
            g = "guess remaining."
        print("{} {:n} {}".format("You have", 5-i, g))

    def in_attempts(self,i):
        a = "attempts."
        if i == 0:
            a = "attempt."
        print("{} {:n} {}".format("\nCorrect! Congratulations, you guessed the word in", i+1, a))
        
    def play(self):
        for x in range(6):
            guess = input("\nEnter guess:")
            while self.check_input(guess):
                guess = input("\nEnter guess:")
            guess = guess.upper()
            self.feedback(self.word,guess)
            if guess == self.word:
                self.in_attempts(x)
                break                            
            self.guesses_remaining(x)
        print("The word was '" + self.word + "'.\n")

    @classmethod
    def end(cls):
        restart = input("Thanks for playing.\nTo play again, enter 'Y' - or to exit, enter 'N':")
        if restart.upper() == "Y":
            cls.start()

Game.start()