dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'


def add_word():
    hun_word = input("Kérlek írd be az előző szó jelentését magyar nyelven: ")
    eng_word = input("Please type in a word: ")
    dictionary[hun_word] = eng_word
    print(dictionary)

add_word()
# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'


#def translate_to_hun(eng_word):
  #  pass


#def translate_to_eng(hun_word):
 #   pass