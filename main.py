


def main():
    with open("books/frankenstein.txt") as f:
        letters_dict = {

            }
        words_count = 0
        file_contents = f.read()
        words = file_contents.split()

        for word in words:
            words_count += 1


        for word_index, word in enumerate(words):
            for letter_index, letter in enumerate(word.lower()):
                if letter in letters_dict:
                    letters_dict[letter]["positions"].append((word_index, letter_index))
                    letters_dict[letter]["count"] += 1
                else:
                    letters_dict[letter] = {
                        "positions": [(word_index, letter_index)],
                        "count": 1
                    }

        # Print the count of each letter
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words_count} words found in the document")
        # Print the count of each letter
        for letter, info in letters_dict.items():
            print(f"Letter '{letter}': {info['count']} times")
        print("____ End report ____")



if __name__ == "__main__":
    main()
