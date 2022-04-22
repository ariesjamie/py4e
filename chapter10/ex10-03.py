# Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
# Find text samples from several different languages and see how letter frequency varies between languages. 
# Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

file = open('words.txt')
dict = dict()
for line in file:
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            #letter = letter.lower()
            dict[letter] = dict.get(letter, 0) + 1
print(dict)

list = []
for k,v in dict.items():
    new_list = (v, k)
    list.append(new_list)
list = sorted(list, reverse=True)
for letter,freq in list:
    print(freq, letter)
