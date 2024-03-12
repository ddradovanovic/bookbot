def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        text = f.read()
        print(get_words_count(text))
        letter_count = count_letters(text)
        print(letter_count)
        sorted_letters = sorting(letter_count)
        print("/////////")
        print(sorted_letters)

def get_words_count(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for letter in text:
        letter = letter.lower()
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def sorting(letters):
    letters_list = []
    for letter in letters:
        letters_list.append({letter:letters[letter]})
    return letters_list


if __name__ == '__main__':
    main()