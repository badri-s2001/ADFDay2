import sys
import os
import uuid
import re

input_file = sys.argv[1]
unique_file = str(uuid.uuid4()) + ".txt"

if os.stat(input_file).st_size == 0:
    print("Input text file is empty")

else:

    prefix_to = []
    end_ing = []
    palindrome = []
    rep_dict = {}
    unique_words = []
    count_dict = {}
    vowel_words = []
    cap_third = []
    cap_fifth = []
    new_lines = []
    new_string = ""

    with open(input_file, mode='r') as f:

        f_contents = f.read()
        list_words = f_contents.split()
        cap_fifth = list_words[::]
        cap_fifth[4] = cap_fifth[4].upper()
        new_string = f_contents.replace(" ", "-")
        new_string = new_string.replace("\n", ";")

        for count, word in enumerate(list_words):

            if word[0:2] == "to":
                prefix_to.append(word)

            if word[-3:] == "ing":
                end_ing.append(word)

            if word == word[::-1]:
                palindrome.append(word)

            if not rep_dict.get(word):
                rep_dict[word] = 1
                unique_words.append(word)

            if rep_dict.get(word):
                rep_dict[word] += 1

            count_dict[count + 1] = word

            split_vowels = re.split('[aeiou]', word)
            vowel_words.append(split_vowels)

            a = list(word)
            a[2] = a[2].upper()
            s = ''.join(a)
            cap_third.append(s)

        print(f"There are {len(prefix_to)} words with prefix 'to'")
        print(f"There are {len(end_ing)} words ending with 'ing'")
        most_rep = max(zip(rep_dict.values(), rep_dict.keys()))[1]
        print(f"The word that was repeated the maximum number of times is '{most_rep}'")
        print(f"The palindromes present in the file are :\n{palindrome}")
        print(f"Unique words in the list are: \n{unique_words}")
        print(f"The counter dict of the file is: \n{count_dict} ")

        f.close()

    with open(unique_file, mode='w') as my_file:
        my_file.write(f"Split the words based on the vowels\n{str(vowel_words)}\n\n")
        my_file.write(f"Capitalize 3rd letter of every word\n{str(cap_third)}\n\n")
        my_file.write(f"Capitalize 5th word of the file\n{str(cap_fifth)}\n\n")
        my_file.write(f"Content after replacing space with '-' and new line with ';'\n{new_string}")

        my_file.close()
