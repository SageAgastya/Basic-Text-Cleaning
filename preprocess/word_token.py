#---First Approach---
import spacy
sp = spacy.load('en_core_web_sm')
line = sp("They\'re surely leaving U.K. for U.S.A. tomorrow")
tokens = [word.text for word in line]
print(tokens)

#---Alternative-1
text = "hey, I found these 2 articles useful: bart, bert."
text = text.split()
print(text)

#----Alternative-2
text = "hey, I found these 2 articles useful: bart, bert."
text = word_tokenize(text)
print(text)
