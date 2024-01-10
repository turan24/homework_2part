with open("homework6.txt", "r") as my_file:
    text_file = my_file.read()

text_file = text_file.split()
clear_list = []

for i in text_file:
    word = i.strip(".,!?:").lower()
    clear_list.append(word)

# words = dict.fromkeys(clear_list)
words = {i: clear_list.count(i) for i in clear_list}

for key, value in words.items():
    print(f"The word '{key}': {value} reps")


