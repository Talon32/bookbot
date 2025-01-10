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
    print("========= Start of Report =========")
    print(f"{count} words found in the document")

def char_count(text):
    text_lowered = text.lower()
    alpha_dict = {}
    char_list = []

    for char in text_lowered:
        if char in alpha_dict:
            alpha_dict[char] += 1
        else:
            alpha_dict[char] = 1
    #return alpha_dict
    for char in alpha_dict:
        if char.isalpha():
            char_dict = {"char": char, "num": alpha_dict[char]}
            char_list.append(char_dict)
            
    def sort_dict(dict):
        return dict["num"]
    
    char_list.sort(reverse=True, key=sort_dict)
    for item in char_list:
        print(f"The {item["char"]} character was found {item["num"]} times.")
    print("========= End of Report =========")

            
main()