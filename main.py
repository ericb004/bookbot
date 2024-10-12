#!/usr/bin/python3

def main():
    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()
        # print(file_contents)
    
    print(word_count(file_contents))

def word_count(text):
    book_list = text.split()
    word_count = len(book_list)
    return word_count





main()