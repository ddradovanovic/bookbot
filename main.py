def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        text = f.read()
        print(get_words_count(text))
        print(count_letters(text))

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

if __name__ == '__main__':
    main()