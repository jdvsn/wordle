class Game:
    def __init__(self, word):
        self.word = word

    @classmethod
    def start(cls):

        import re

        game = Game("photo")
        
        guesses = ["5","4","3","2","1","0"]

        print("Welcome to Wordle!")
        
        for x in guesses:

            guess = input("Enter guess:")

            while re.findall("[^a-zA-Z]", guess) :
                print("Your guess must only contain letters - try again.")
                guess = input("Enter guess:")

            while len(guess) != 5:
                print("Your guess must be 5 letters - try again.")
                guess = input("Enter guess:")

            if guess == game.word:
                print("Congratulations!")
                break
            
            print(("You have ") + x + (" guesses left."))
            
        print("Thanks for playing.")

Game.start()
