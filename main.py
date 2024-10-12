#!/usr/bin/python3

def main():
    book = './books/frankenstein.txt'
    with open(book) as f:
        file_contents = f.read()
        # file_contents = 'mississippi'
        # print(file_contents)
    
    print(word_count(file_contents))
    print(big_char_counter(file_contents))

def word_count(text):
    book_list = text.split()
    word_count = len(book_list)
    return word_count

def big_char_counter(text):
    text_lowered = text.lower()
    count_holder = {}
    for thing in text_lowered:
        if thing in count_holder:
            # print(f"I see {count_holder[thing]}")
            count_holder[thing] +=1
            # print(count_holder)
        else:
            count_holder[thing] = 1
            # print(f"First find: {count_holder[thing]}")
    return count_holder



main()