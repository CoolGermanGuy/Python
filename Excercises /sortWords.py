import re
exampleArray = ["apple", "banana", "CoolGermanGuy", "I", "don't", "LIKE", "ThE", "gOvErNmEnT"]
def sortWordsAlphabetically(array):
  # remove special characters
  for i in array:
    array[i] = re.sub(r'[^a-zA-Z0-9\s]', '', array[i])
  # make everything lowercase
  for i in array:
    array[i] = array[i].lower()
  # sort em
