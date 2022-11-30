myfile = open("my_txt_file.txt", "r")

d = dict()

for sentence in myfile:
    sentence = sentence.lower().replace('.', '').replace(',', '')
    words = sentence.split(" ")
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

for key in list(d.keys()):
    print(key, ":", d[key])

# Description of what I have done above:
# First of all, I made all words lowercase and removed two special signs appearing in the file from the future
# calculations.
# Then, I used split() function to split strings into a list of words.
# Then, I needed to iterate over every word in my file and check if the word already exists in my dictionary.
# If so, the count of this particular word was increased by 1.
# If not, new word was added to dictionary and counted as 1.
# Lastly, I printed out the content of a dictionary.