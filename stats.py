def count_words(book):
    words_list = book.split()
    return len(words_list)

def count_characters(book):
    characters_dictionary = {}
    for character in book:
        lower_character = character.lower()
        if lower_character in characters_dictionary:
            characters_dictionary[lower_character] += 1
        else:
            characters_dictionary[lower_character] = 1
    return characters_dictionary

def sorted_chars(total_characters):
    list_charnums = []
    for char,num in total_characters.items():
        if char.isalpha():
            char_dict = {"char": char, "num": num}
            list_charnums.append(char_dict)
    list_charnums.sort(reverse=True, key=sort_on)
    return list_charnums

def sort_on(dict_entry):
    return dict_entry['num']


