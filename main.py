with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def main():
    awesome_aah_output(count_characters_in_string(file_contents), count_words(file_contents))

def count_words(text): 
    splitted_string = text.split()
    return len(splitted_string)

def count_characters_in_string(string):
    lowered_string = string.lower()
    straight_string = lowered_string.replace(" ", "")
    unique_symbols_arr = []
    for symbol in straight_string:
        if symbol not in unique_symbols_arr:
            unique_symbols_arr.append(symbol)

    symbols_dict = {}
    for symbol in unique_symbols_arr:
        symbols_dict[symbol] = straight_string.count(symbol)
    return symbols_dict

def awesome_aah_output(symbols_dict, word_count):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for symbol, count in symbols_dict.items():
        print(f"The {symbol} character was found {count} times")
    print("--- End report ---")
main()