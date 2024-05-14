import re
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
  # sort em
  for word in middleArray:
    
