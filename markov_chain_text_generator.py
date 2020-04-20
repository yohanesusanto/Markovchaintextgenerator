# https://blog.upperlinecode.com/making-a-markov-chain-poem-generator-in-python-4903d0586957
# I found this on the web where a text-file is read, first. Following this, for each word in 
# the text-file as key, a Python-Dictionary of words-that-immediately-followed-the-key was 
# constructed.  We start from a random-initial-key and pick (at random) the next-word from 
# the dictionary (using the first-word as key).  This process repeats till sufficient words 
# of text have been generated.

import random
import sys
import argparse

# have to remove multiple occurrences of spaces etc in the training text 
def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

# form a single string that contains the entire novel as training data... 
INPUT_FILENAME = str(sys.argv[1])
#INPUT_FILENAME = 'thegreatgatsby'
training_text = open(INPUT_FILENAME, "r").read()
#training_text = open(INPUT_FILENAME, "r", encoding = "ISO-8859-1").read()

# split the string into its constituent words (got this part from the web)
training_text = ''.join([i for i in training_text if not i.isdigit()]).replace("\n", " ").split(' ')
# This process the list of poems. Double line breaks separate poems, so they are removed.
# Splitting along spaces creates a list of all words.

# remove blank-spaces 
training_text = remove_values_from_list(training_text, '')
training_text = remove_values_from_list(training_text, ' ')

# the length of the generated text 
generated_text_length = int(sys.argv[2])+0
#generated_text_length = 200 
index = 1
chain = {}

# This loop creates a dictionary called "chain". Each key is a word, and the value of each key
# is an array of the words that immediately followed it.
for word in training_text[index:] : 
    key = training_text[index - 1]
    if key in chain :
        chain[key].append(word)
    else:
        chain[key] = [word]
    index += 1

#random first word
word1 = random.choice(list(chain.keys())) 
message = word1.capitalize()

# Picks the next word over and over until word count achieved
while len(message.split(' ')) < generated_text_length:
    word2 = random.choice(chain[word1])
    word1 = word2
    message += ' ' + word2

#OUTPUT_FILENAME = str(sys.argv[3])
OUTPUT_FILENAME = 'output.txt'

# creates new file with output
with open(OUTPUT_FILENAME, "w") as file:
    file.write(message)
    
#uncomment rows below to print it in the terminal    
#output = open(OUTPUT_FILENAME,"r")
#print(output.read())
