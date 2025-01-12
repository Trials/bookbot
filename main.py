def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    word_count = count_characters(text)
    sorted_char_count = sorted(word_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")

    for item in sorted_char_count:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")



def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    words = {}
    for c in text:
        lowered = c.lower()
        if lowered not in words:
            words[lowered] = 1
        else:
            words[lowered] = words.get(lowered) + 1
    return words

def sort_on(d):
    return d["num"]      

def sorted(dict):
    sorted_list = []
    for character in dict:
        sorted_list.append({"char": character, "num": dict[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()