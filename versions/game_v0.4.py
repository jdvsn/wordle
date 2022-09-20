class Game:
    def __init__(self, word):
        self.word = word

    @classmethod
    def start(cls):

        import re
        import getpass

        print("Welcome to Wordle!")

        word = getpass.getpass("Enter Word:")

        game = Game(word)
        
        guesses = ["5","4","3","2","1","0"]
        
        for x in guesses:

            guess = input("Enter guess:")

            while re.findall("[^a-zA-Z]", guess) or len(guess) != 5:
                print("Invalid guess - try again.")
                guess = input("Enter guess:")
         
            if guess == game.word:
                print("Congratulations!")
                break
            
            print(("You have ") + x + (" guesses left."))
            
        print("Thanks for playing.")

Game.start()
