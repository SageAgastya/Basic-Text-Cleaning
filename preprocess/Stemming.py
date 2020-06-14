#---First Approach--
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
text = "hey, I found these 2 articles useful: bart, bert."
tokens = [token for token in text.split()]
stemmed = [porter.stem(word) for word in tokens]
print(stemmed)

#---Alternative---
from nltk.stem.snowball import SnowballStemmer
snowball = SnowballStemmer(language="english")
text = "hey, I found these 2 articles useful: bart, bert."
tokens = [token for token in text.split()]
stemmed = [snowball.stem(word) for word in tokens]
print(stemmed)
