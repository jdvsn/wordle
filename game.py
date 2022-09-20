import re
import getpass
import string
from dictionary import Dictionary
from time import sleep

class Game:
    GUESSES = 6
    def __init__(self, word):
        self.word = word
        self.alphabet = list(string.ascii_lowercase)
        self.guesses_made_list = []
        self.guesses_made = len(self.guesses_made_list)
        self.guesses_left = Game.GUESSES - self.guesses_made

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
        def feedback_character(word_list,guess_list):
            if guess_list == word_list:
                return "!"
            if guess_list in word:
                return "?"       
            return "_"
        feedback_list = list(map(feedback_character,list(word),list(guess)))
        print(" ".join(list(guess)) + "\n" +  " ".join(feedback_list) + "\n")
        
    def alphabet_feedback(self,word,guess):
        al = self.alphabet
        gl = list(guess.lower())
        wl = list(word.lower()) 
        for x in gl:
            if x not in al:
                continue
            al_index = al.index(x)
            al.remove(x)
            if x in wl:
                al.insert(al_index,x.upper())
            else:
                al.insert(al_index,"_")
        print(" ".join(al))
 
    def guesses_remaining(self):
        g = "guesses"
        if self.guesses_left == 1:
            g = "guess"
        print(f"You have {self.guesses_left} {g} remaining.")

    def in_attempts(self):
        a = "attempts"
        if self.guesses_made == 1:
            a = "attempt"
        print(f"\nCorrect! Congratulations, you guessed the word in {self.guesses_made} {a}.")
    def make_guess(self):
        guess = input("Enter guess:")
        while self.check_input(guess):
            guess = input("\nEnter guess:")
        guess = guess.upper()
        self.guesses_made_list.append(guess)
        self.guesses_made = len(self.guesses_made_list)
        self.guesses_left = Game.GUESSES - self.guesses_made
        return guess
        
    def check_success(self,word,guess):
        if guess == word:
            self.in_attempts()
            return True                                        
        self.guesses_remaining()

    def end_feedback(self):
        print(f"The word was '{self.word}'.\n")
        view_list = input("To view your guesses, enter 'Y' - otherwise, enter 'N':")
        if view_list.lower() == "y":
            print(("Your guesses were:\n") + "\n".join(self.guesses_made_list))

    def play(self):
        # until the game is solved
        # ask the user for a word
        # check word for success
        # give feedback
        for x in range(Game.GUESSES):
            guess = self.make_guess()
            if self.check_success(self.word,guess):
                break
            self.feedback(self.word,guess)
            self.alphabet_feedback(self.word,guess)
        self.end_feedback()
        
        
    @classmethod
    def end(cls):
        restart = input("To play again, enter 'Y' - or to exit, enter 'N':")
        if restart.upper() == "Y":
            cls.start()
        else:
            print("Thanks for playing!")
            sleep(1)

Game.start()