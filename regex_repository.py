import re

def adapt_title_for_windows(title):
    return re.sub("\t|\n|:", "", title)

def eliminate_special_characters(text):
    return re.sub("\t|\n", "", text)
