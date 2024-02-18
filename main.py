def main():
    book_path = "books/frankenstein"
    text = book_text(book_path)
    num_words = word_num(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = sorted_list(chars_dict)

    full_text = input("do you want the file printed in report? (y/n)   ")
    words = input("Do you want the number of words printed in the report? (y/n)   ")
    letters = input("do you want the letter count found in the file in the report? (y/n)   ")
    if full_text == "y":
        print(f"full text of file {book_path}")
        print(text)
    
    print()
    print()
    print()
    print(f"Report for file {book_path} ")
    print()

    if words == "y":
        print(f"There are {num_words} words found in the file")
    

    if letters == "y":
        print()
        print("Letters found in order of most to least common:")
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


def sorted_list(num_chars_dict):
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


def book_text(path):
    with open(path) as f:
        return f.read()


main()