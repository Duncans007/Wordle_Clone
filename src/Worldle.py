# Game object for worldle, self-contained
# Word dictionary from http://www.gwicks.net/dictionaries.htm

from random import randint
from codecs import open

class Worldle:
    def __init__(self, word_length=5, max_guesses=6, dictionary_txt="ext\dictionary.txt"):

        self.word_length = word_length
        self.max_guesses = max_guesses
        self.guesses = 1

        self.word_solution = ""

        self.word_list = self.import_words(dictionary_txt)
        self.generate_word()


    ##### Using a complete alpha dictionary, import all words with correct number of letters
    def import_words(self, dict_file):
        words = open(dict_file, encoding='iso-8859-1').read().splitlines()
        for i in range(len(words)-1, -1, -1):
            if len(words[i]) != self.word_length and words[i].isascii():
                words.pop(i)
        return words


    ##### Generate new word using pseudo-random generator, reset guesses
    def generate_word(self):
        idx = randint(0, len(self.word_list)-1)
        self.word_solution = self.word_list[idx]
        #self.word_list.pop(idx)
        self.guesses = 1
        self.taking_guesses = True


    ##### Function steps forward when a guess is taken by inputting to this function
    def guess(self, word_guess):
        if self.taking_guesses:
            ##### Return codes
            # 0: successfully made guess
            # 1: last guess taken, show word
            # 2: guess word not proper length
            # 3: guess word not an actual word
            # 4: guessed word correctly
            # 5: is not alpha

            ##### Check for error codes
            # Make sure the word is letters only
            if not word_guess.isalpha():
                return [5, "Error 5: Word is not letters only. Please try again with letters only."]

            # Make sure the word is the proper length
            if len(word_guess) != self.word_length:
                return [2, f"Error 2: Word is not proper length. Please try again with word length of {self.word_length}."]

            # Check if word is in dictionary of valid words
            if word_guess not in self.word_list:
                return [3, "Error 3: Word is not in dictionary of valid words."]


            ##### Check words for matching letters
            matched_output = []
            self.guesses = self.guesses + 1
            for g, s in zip(word_guess, self.word_solution):
                # Test for matching letters in proper place
                if g == s:
                    matched_output.append(1)
                # Test for matching letters in improper place
                elif g in self.word_solution:
                    matched_output.append(2)
                # If neither condition is satisfied, letter does not exist
                else:
                    matched_output.append(0)


            ##### Check for perfectly matching words
            if matched_output == [1]*self.word_length:
                return [4, matched_output]


            ##### Send solution if max guesses is reached
            if self.guesses <= self.max_guesses:
                return [0, matched_output]
            else:
                output_word = self.word_solution
                self.taking_guesses = False
                return [1, matched_output, output_word]


    def output_to_colors(self, matched_outp, colors=['gray', 'green', 'yellow']):
        outp = []
        for i in range(0, len(matched_outp)):
            outp.append(colors[matched_outp[i]])
        return outp
