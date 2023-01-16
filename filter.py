
# Filtering words into number, term, and def
# list of strings -> list of dictionaries
# output format: [{number: ..., term: ..., def: ...}, {...}, ...]
def filter_words(raw_words):
    words = []
    current_word = {}
    counter = 0

    for i in range(len(raw_words)):
        word = raw_words[i]
        key = ""
        counter += 1

        if counter == 1:
            current_word["number"] = word
        elif counter == 2:
            current_word["term"] = word
        elif counter == 3:
            current_word["def"] = word
            counter = 0
            words.append(current_word)
            current_word = {}
    
    return words

# Filters raw text into a list of dictionaries with the keys
# 'number', 'term', and 'def'
# string -> list of dictionaries
#    "text" variable should be a string written in format:
#    "<number> <word in target language> <word in en>"
def filter_text(text):
    # filtering out weird non-space whitespace chars
    t = text.replace("	", " ")
    # converting text to list
    raw_words = t.split(" ")

    return filter_words(raw_words)

# Checks list of cards based on card number to make sure
# that it's formatted correctly
def check_cards(cards, print_all = False):
    def represents_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    for card in cards:
        if not represents_int(card["number"]):
            print(f"Card formatted incorrectly with value: {card['number']}")
            return False
        elif print_all:
            print("card passed!:")
            print(card)
    return True