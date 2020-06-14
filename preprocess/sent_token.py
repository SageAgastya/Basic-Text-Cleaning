#----first approach---
import spacy

sp = spacy.load('en_core_web_sm')
document = sp("Hello how are you. Go for work. What do you want?")
sents = [str(sentence) for sentence in document.sents]
print(sents)

#----Alternative-----
from nltk.tokenize import sent_tokenize
document = "Hello how are you. Go for work. What do you want?"
sents = sent_tokenize(document)
print(sents)
