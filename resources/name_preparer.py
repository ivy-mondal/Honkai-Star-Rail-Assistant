import re

def name_prepares(string):
    words = re.findall(r'[a-zA-Z0-9]+', string)
    uppercased_words = [word.upper() for word in words]
    return "_".join(uppercased_words)

print(name_prepares("The Wondrous BananAmusement Park"))

