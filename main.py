#!/usr/bin/python3

def main():
    book = './books/frankenstein.txt'
    with open(book) as f:
        file_contents = f.read()
        # file_contents = 'mississippi'
        # print(file_contents)
    
    w_count = word_count(file_contents)
    ch_count = big_char_counter(file_contents)

    book_report(book, w_count, ch_count)

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

# def book_report(title, wcount, chcount):
#     print(f"*** Begin book report of {title} ***")
#     print(f"{wcount} words found in the document")
#     alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
#                 'o','p','q','r','s','t','u','v','w','x','y','z']
#     for letter in alphabet:
#         if letter in chcount:
#             print(f"The '{letter}' character was found {chcount[letter]} times")
#         else:
#             print(f"The {letter} character was found 0 times")


#title is a string; #wcount is an int, #chcount is a dictionary
def book_report(title, wcount, chcount):
    print(f"*** Begin book report of {title} ***\n")
    print(f"{wcount} words found in the document\n")
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                'o','p','q','r','s','t','u','v','w','x','y','z']
    sorted_alphabet = []
    for letter in alphabet:
        if letter in chcount:
            sorted_alphabet.append({"name":letter, "num":chcount[letter]})
        sorted_alphabet.sort(reverse=True, key=sort_on)
    # print(sorted_alphabet)
    for thing in sorted_alphabet:
        # print(f"The {thing['name']} character was found {thing['num']} ")
        print(f"Count of the the letter {thing['name']} is {thing['num']}")

def sort_on(dict):
    return dict['num']

main()

"""The key parameter in Python's sort() and sorted() functions is a special case.
When you pass a function as the key argument, Python doesn't call that function immediately. Instead, it uses the function as a "callback" or a "mapper".
Here's what happens:

    Python iterates over the list of items to be sorted (sorted_alphabet in your case).
    For each item, Python calls the key function (sort_on), passing the item as an argument.
    The key function returns a value, which is used for sorting purposes.

In your case:

    sorted_alphabet is a list of dictionaries, e.g., {"name": "a", "num": 10}.
    The key function sort_on takes a dictionary as an argument.
    When Python iterates over sorted_alphabet, it calls sort_on for each dictionary, passing the dictionary as an argument.
    sort_on returns the value associated with the "num" key (dict['num']).
    Python uses these returned values to determine the sort order.

The reason you don't need to pass an argument explicitly when using key=sort_on is that Python handles the function call internally."""

