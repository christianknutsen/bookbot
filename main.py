def main():
    book_path = "books/frankenstein"
    text = get_book_text(book_path)
    num_words = word_num(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"full text of file {book_path}")
    print(text)
    print()
    print()
    print()
    print(f" Report of words for file {book_path} ")
    print()
    print(f"There are {num_words} words found in the file")
    print()
    print("letters found in order of most to least common:")
    print()
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The letter '{item['char']}' was found in the file {item['num']} times")

    print()
    print("Report finished")


def word_num(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()