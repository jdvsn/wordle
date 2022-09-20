import random
import urllib.request

class Dictionary:
    def __init__(self, file_path):
        self.file_path = file_path
        if "/" in self.file_path:
            req = urllib.request.Request(self.file_path)
            response = urllib.request.urlopen(req)
            the_page = response.read()
            words = the_page.decode().split("\n")
            filter_fn = lambda word: len(word) == 5
            filter(filter_fn, words)
            self.wordlist = list(filter(filter_fn,words))
        elif "\\" in self.file_path:           
            self.wordlist = open(self.file_path,"r")
            self.wordlist = self.wordlist.readlines()
            self.wordlist = list(map(lambda word: word.rstrip(), self.wordlist))

    def choose_word(self):
        return random.choice(self.wordlist) 