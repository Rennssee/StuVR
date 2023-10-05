import re


def find_all_words(text, word):
    s = re.findall(word, text, flags=re.IGNORECASE)
    return s


text = "Python is great. I love python. pYthoN is awesome. Isn't PYTHOn wonderful?"
word = "python"

print(find_all_words(text, word))
