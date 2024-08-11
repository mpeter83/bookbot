def get_text(file):
    with open(file) as f:
        content = f.read()
        return content


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    chars = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in chars.keys():
            tmp = chars[char]
            chars[char] = tmp + 1
        else:
            chars[char] = 1
    return chars


def print_stat(dict):
    for element in sorted(dict, key=dict.get, reverse=True):
        if element.isalpha():
            print(f"The '{element}' char was found {dict[element]} times")


def main():
    book_path = "books/frankenstein.txt"
    book_content = get_text(book_path)
    # print(book_content)
    chars = count_characters(book_content)
    print(f"==== Report of {book_path} ====")
    print(f"There are {count_words(book_content)} words in the document.\n")
    print_stat(chars)
    print("==== End report ====")


main()
