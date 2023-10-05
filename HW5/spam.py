import re


def replace_spam_words(text, spam_words):
    # p = re.sub(r'(blue|white|red)', 'color', 'blue socks and red shoes')

    res = re.findall(spam_words, text, re.IGNORECASE)


text = "Hello world, FU, sex, Love, SS"
spam_words = "sex", "FU"

print(replace_spam_words(text, spam_words))
