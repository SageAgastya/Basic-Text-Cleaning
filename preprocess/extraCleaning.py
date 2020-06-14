#---------------------extra note
import unicodedata
text = "ārtīclē ṇūṁbēr̥ 101"
tokens = word_tokenize(text)
temp = [unicodedata.normalize("NFD",token).encode("ascii","ignore").decode("utf8") for token in tokens]
print(temp)
