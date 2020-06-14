import spacy

#------first approach---
sp = spacy.load('en_core_web_sm')
sentence = sp("hey, I found these 2 articles useful: bart, bert.")
temp = [(word.text,  word.lemma_) for word in sentence]
print(temp)

#------Alternative------
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()
sentence = "hey, I found these 2 articles useful: bart, bert."
temp = [(word,lemmatizer.lemmatize(word)) for word in word_tokenize(sentence)]
print(temp)
