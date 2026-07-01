import requests
import re

url = 'http://www.gutenberg.org/files/1112/1112.txt'

text = requests.get(url).text.lower() # download the text

words = re.findall(r'[a-z]+', text) # extract words

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Sort the words by frequency
sorted_words = sorted(word_count.items(), key = lambda item: item[1], reverse = True)

# Print the 10 most common words
for word, count in sorted_words[:10]:
    print(f'{word}: {count}')
    










