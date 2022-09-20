# Uses wordlist.txt to get a word

import re
from dictionary import Dictionary

class Game:
    def __init__(self, word):
        self.word = word

    @classmethod
    def start(cls):

        print("Welcome to Wordle!")

        word = Dictionary("C:\\Users\\joeda\\coding\\wordle-app\\wordlist.txt").choose_word()
        word = word.lower()

        word_list = list(word)
        # wl stands for word_list
        wl_1 = word_list[0]
        wl_2 = word_list[1]
        wl_3 = word_list[2]
        wl_4 = word_list[3]
        wl_5 = word_list[4]

        guesses = 6
        
        for x in range(guesses):

            guess = input("Enter guess:")
            guess = guess.lower()

            while re.findall("[^a-zA-Z]", guess) or len(guess) != 5:
                print("Invalid guess - try again.")
                guess = input("Enter guess:")
         
            if guess == word:
                print(("Congratulations, you guessed the word in ") + str(x+1) + (" attempt(s)."))
                break
            
            guess_list = list(guess)
            # gl stands for guess_list
            gl_1 = guess_list[0]
            gl_2 = guess_list[1]
            gl_3 = guess_list[2]
            gl_4 = guess_list[3]
            gl_5 = guess_list[4]

            # fb stands for feedback
            fb_1 = ("_")
            fb_2 = ("_")
            fb_3 = ("_")
            fb_4 = ("_")
            fb_5 = ("_")

            if gl_1 == wl_1:
                fb_1 = ("!")
            elif gl_1 == wl_2:
                fb_1 = ("?")
            elif gl_1 == wl_3:
                fb_1 = ("?")
            elif gl_1 == wl_4:
                fb_1 = ("?")
            elif gl_1 == wl_5:
                fb_1 = ("?")
            
            if gl_2 == wl_2:
                fb_2 = ("!")
            elif gl_2 == wl_1:
                fb_2 = ("?")
            elif gl_2 == wl_3:
                fb_2 = ("?")                
            elif gl_2 == wl_4:
                fb_2 = ("?")
            elif gl_2 == wl_5:
                fb_2 = ("?")

            if gl_3 == wl_3:
                fb_3 = ("!")
            elif gl_3 == wl_1:
                fb_3 = ("?")
            elif gl_3 == wl_2:
                fb_3 = ("?")
            elif gl_3 == wl_4:
                fb_3 = ("?")
            elif gl_3 == wl_5:
                fb_3 = ("?")

            if gl_4 == wl_4:
                fb_4 = ("!")
            elif gl_4 == wl_1:
                fb_4 = ("?")
            elif gl_4 == wl_2:
                fb_4 = ("?")
            elif gl_4 == wl_3:
                fb_4 = ("?")
            elif gl_4 == wl_5:
                fb_4 = ("?")

            if gl_5 == wl_5:
                fb_5 = ("!")
            elif gl_5 == wl_1:
                fb_5 = ("?")
            elif gl_5 == wl_2:
                fb_5 = ("?")
            elif gl_5 == wl_3:
                fb_5 = ("?")
            elif gl_5 == wl_4:
                fb_5 = ("?")

            print((fb_1) + (fb_2) + (fb_3) + (fb_4) + (fb_5))
            if x == 5:
                print("You have 1 guess remaining.")
            else:               
                print(("You have ") + str(5-x) + (" guesses remaining."))
        print(("The word was ") + word + ("."))
        print("Thanks for playing.")

Game.start()
