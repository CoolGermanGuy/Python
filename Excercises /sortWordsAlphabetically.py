import re
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

exampleArray = ["apple", "banana", "CoolGermanGuy", "I", "don't", "LIKE", "ThE", "gOvErNmEnT"]
middleArray = []
sortedArray = []
def sortWordsAlphabetically(array):
  # remove special characters
  for word in array:
    middleArray[word] = re.sub(r'[^a-zA-Z0-9\s]', '', array[word])
  # make everything lowercase
  for word in middleArray:
    middleArray[word] = middleArray[word].lower()
  # SORT PROCESS
  for word in middleArray: # each word
    # assign numbers
    numberArray = []
    for char in middleArray[word]: # each character
      # assign numeric values
      numberArray.append(characters.index(char))
  
