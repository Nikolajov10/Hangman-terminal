from random_word import RandomWords

class HangmanGame:
    generator = RandomWords()
    NUM_TRYS = 5

    def __init__(self):
        self.score = 0
        self.mistakes = 0
        self.word = ""
        self.end = False
        self.hits = 0

    def __checkWord(word) -> bool:
        '''
        return true if word contains only letters
        false otherwise
        :return:
        '''
        if not word: return False

        for letter in word:
            if not letter.isalpha():
                return False

        return True

    def startGame(self):
        self.mistakes = 0
        self.hits = 0
        self.end = False
        self.word = HangmanGame.generator.get_random_word()
        while  not HangmanGame.__checkWord(self.word):
            if not self.word:
                HangmanGame.generator = RandomWords()
            self.word = HangmanGame.generator.get_random_word()

    def checkLetter(self,letter)->list[int]:
        '''
        returns positions of letter in word and
        increments hit for every hit
        else returns None and increments mistakes
        :param letter: char
        :return:
        '''
        positions = None

        for index,word_let in enumerate(self.word):
            if word_let == letter:
                self.hits += 1
                if not positions:
                    positions = [index]
                else:
                    positions.append(index)
        if not positions:
            self.mistakes += 1
        if self.mistakes == HangmanGame.NUM_TRYS or self.hits == len(self.word):
            self.end = True
        return positions

    def checkWord(self,word):
        '''
        checking if word is correct
        :param word: string
        :return:
        '''
        if word == self.word:
            self.hits = len(self.word)
            self.end = True
        else:
            self.mistakes += 1
            if self.mistakes == HangmanGame.NUM_TRYS:
                self.end = True

    def isEnd(self)-> bool:
        return self.end

    def endGame(self)->str:
        message = ""
        if self.hits == len(self.word):
            self.score += 1
            message = "You win!"
        else:
            message = "You lost!"
        message += " The word was: " + self.word + "\nScore: " + str(self.score)
        return message

    def getScore(self)->int:
        return self.score

    def getWord(self)->str:
        return self.word

    def getMistakes(self)->int:
        return self.mistakes
