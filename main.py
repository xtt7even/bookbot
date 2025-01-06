with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def main():
    count = count_words(file_contents)

    count_characters_in_string(file_contents)

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
    print(unique_symbols_arr)

    symbols_dict = {}
    for symbol in unique_symbols_arr:
        symbols_dict[symbol] = straight_string.count(symbol)
    print(symbols_dict)      

main()