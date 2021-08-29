class WordError(Exception):
    pass

def check_w_letter(word):
    for letter in word:
        if letter == "w":
            raise WordError

    return word
