with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def main():
    count = count_words(file_contents)
    print(count)

def count_words(string): 
    splitted_string = string.split()
    return len(splitted_string)

main()