def main():

    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    word_count(file_content)
    char_count(file_content)

def word_count(text):
      
    words_split = text.split()
    count = 0
    for word in words_split:
         count += 1
    print(f"{count} words found in the document")

def char_count(text):
    text_lowered = text.lower()
    alpha_dict = {}

    for char in text_lowered:
        if char in alpha_dict:
            alpha_dict[char] += 1
        else:
            alpha_dict[char] = 1
    return alpha_dict

            
main()