class CrilicToEnglish:
    alphabet = {'а': 'a', 'б': 'b', ' ':' ', ',':',', '.':'.', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'y', 'ҷ':'j', 'ӯ':'u', 'қ':'q', 'ҳ':'h', 'ӣ':'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}
    
    def __init__(self, word):
        '''
        # ABC 
        # abs
        # Abc
        '''
        self.word = word
        
    def translate(self, option=None):
        new_word = ''
        if option == 'ABC':
            for letter in self.word.lower():
                if letter in self.alphabet:
                    new_word += self.letterOption(self.alphabet[str(letter)], 'upper')
            return new_word
        
        elif option == 'Abc':
            for letter in self.word.lower():
                if letter in self.alphabet:
                    new_word += self.letterOption(self.alphabet[str(letter)], 'capitalize')
            return new_word.title()
        
        else:
            for letter in self.word.lower():
                if letter in self.alphabet:
                    new_word += self.letterOption(self.alphabet[str(letter)], 'lower')
            return new_word
        
    def letterOption(self, letter, option):
        if option == "upper":
            return letter.upper()
        elif option == "lower":
            return letter.lower()
        else:
            return letter

    def slugify(self, pattern):
        words = self.translate(pattern).split(" ")
        slugified_word = ''
        for index, word in enumerate(words):
            if index < len(words)-1:
                slugified_word += f"{word}_"
            else:
                slugified_word += f"{word}"
        return slugified_word