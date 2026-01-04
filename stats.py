def count_words(text):
    return len(text.split())

def count_letters(text):
    letters_count = {}

    for char in text:
        if char.lower() in letters_count:
            letters_count[char.lower()] += 1
        else:
            letters_count[char.lower()] = 1

    return letters_count

def sort_on(items):
    return items["num"]

def create_pretty(chars_dict):
    new_structure_chards_dict = []

    for char in chars_dict:
        new_structure_chards_dict.append({ "char": char, "num": chars_dict[char] })
    
    new_structure_chards_dict.sort(reverse=True, key=sort_on)

    return new_structure_chards_dict