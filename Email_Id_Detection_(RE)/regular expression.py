import re

# Regex that can match words that start with im or ends with ed
reg = re.compile(r'^[i]{1}[m]{1}[a-z]*|[a-z]*[e]{1}[d]{1}$')

words = ['impossible', 'trimming', 'interim', 'immature', 'evacuated', 'education', 'showed', 'predetor']

# extract the words that match the regex
matched_words = list(filter(reg.match, words))

# Display the matched words
print('Matched Words are: ')
for values in matched_words:
	print(values)

