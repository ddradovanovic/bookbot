def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        text = f.read()
        word_count = get_words_count(text)
        letter_count = count_letters(text)
        # print(letter_count)
        letters_list = list_letters(letter_count)
        # Sorting the list of letters based on the amount of time they shown up
        letters_list.sort(reverse=True, key=sort_on)
        build_report(word_count, letters_list)

def get_words_count(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for letter in text:
        letter = letter.lower()
        if letter.isalpha():
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def list_letters(letters):
    letters_list = []
    for letter in letters:
        letters_list.append({"letter":letter, "value":letters[letter]})
    return letters_list

def sort_on(dictionary):
    return dictionary["value"]


def build_report(word_count, list_sorted):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"There are {word_count} words found in the document\n")

    for i in range(0, len(list_sorted) - 1):
        print(f"The {list_sorted[i]['letter']} character was found {list_sorted[i]['value']} times.")


if __name__ == '__main__':
    main()