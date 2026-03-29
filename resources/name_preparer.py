import re

def name_prepares_upper(string):
    words = re.findall(r'[a-zA-Z0-9]+', string)
    uppercased_words = [word.upper() for word in words]
    return "_".join(uppercased_words)

print(name_prepares_upper("The Finale of a Lie"))

def name_prepares_lower(string):
    words = re.findall(r'[a-zA-Z0_9]+', string)
    lowercased_words = [word.lower() for word in words]
    return "_".join(lowercased_words)

print(name_prepares_lower("Elation Brimming With Blessings"))
print(name_prepares_lower("The Finale of a Lie"))
print(name_prepares_lower("Today's Good Luck"))
print(name_prepares_lower("Thus Burns the Dawn"))



