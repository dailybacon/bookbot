def main():

    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path) 
    word_count = get_word_count(text)
    character_count = count_characters(text)
    list_of_dicts = list_character_count(character_count)
    
    print_report(file_path, word_count, list_of_dicts)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    text = text.split()
    return len(text)

def count_characters(words):
    char_dictionary = {}
    text_string = str(words.lower())

    for letter in text_string:
        if letter in char_dictionary:
            char_dictionary[letter] += 1
        else:
            char_dictionary.update({letter: 1})
    
    return(char_dictionary)

def sort_on(dict):
    return next(iter(dict.values()))

def list_character_count(char_dict):
    dict_to_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            dict_to_list.append({key: value})
    dict_to_list.sort(reverse=True, key=sort_on)
    return dict_to_list

def print_report(file, no_of_words, list_of_dicts):
    print(f'--- Begin report of {file} ---')
    print(f"{no_of_words} words found in the document.\n")
    for i in list_of_dicts:
        for k in i:
            print(f'There are {i[k]} occurences of the letter \'{k}\'. ')
        
    print(f'--- End report ---')

main()