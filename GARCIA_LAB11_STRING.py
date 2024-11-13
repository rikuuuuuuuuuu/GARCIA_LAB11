#GARCIA_LAB11_STRING

word_list = []
print("Enter 10 words (press Enter after each word):")

print("===========================")

while len(word_list) < 10:  
    word = input("Enter word: ")
    
    if len(word_list) >= 10 and word.lower() == 'done': 
        break
        
    if word: 
        word_list.append(word)
        
    if len(word_list) < 10:  
        print(f"Please enter {10 - len(word_list)} more words")

min_length = int(input("Enter a number: "))

print("===========================")

found_words = []
for word in word_list:
    if len(word) >= min_length:
        found_words.append(word)
        continue
    print(f"{word} is only {len(word)} letters - too short")

print("===========================")

if found_words:
    print(f"Words with {min_length} or more letters:")
    for word in found_words:
        print(f"{word} - {len(word)} letters")
else:
    print(f"No words with {min_length} or more letters found")
