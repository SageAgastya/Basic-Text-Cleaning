#---First Approach---
import string
import re

text = "hey, I found these two articles useful: bart, bert."
text = text.split()
text = [re.sub("["+string.punctuation+"]", "", word) for word in text]
print(text)

#ALTERNATIVE-1
text = "hey, I found these two articles useful: bart, bert."
text = text.split()
table = str.maketrans("","",string.punctuation)
text = [word.translate(table) for word in text]
print(text)


#ALTERNATIVE-2
from nltk.tokenize import word_tokenize

text = "hey, I found these 2 articles useful: bart, bert."
text = word_tokenize(text)
text = [word for word in text if word.isalnum()]
print(text)
