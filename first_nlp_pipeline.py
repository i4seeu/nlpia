#simplest way to tokenize is to use white spaces using the split method
#Tokenization
sentence = "Thomas Jefferson began building Monticello at the age of 26."
# print(sentence.split())
# #or
# print(str.split(sentence))
import numpy as np 
import pandas as pd
token_sequence = str.split(sentence)
vocab = sorted(set(token_sequence))

num_tokens = len(token_sequence)
vocab_size = len(vocab)

onehot_vectors = np.zeros((num_tokens,vocab_size),int)
for i, word in enumerate(token_sequence):
    onehot_vectors[i, vocab.index(word)] = 1

df = pd.DataFrame(onehot_vectors, columns=vocab)

#using bag of words rather simple tokenization because of issues to do with memory
sentence_bow = {}
for token in sentence.split():
    sentence_bow[token] = 1
df_b = pd.DataFrame(pd.Series(dict([(token,1) for token in sentence.split()])),columns=['sent']).T

#constructing  a dataframe of bag-of-words vectors with multiple sentences

sentences = "Thomas Jefferson began building Monticello at the age of 26.\n"
sentences += "Construction was done mostly by local masons and carpenters.\n"
sentences += "He moved into the South Pavilion in 1770.\n"
sentences += "Turning Monticello into a neoclassical masterpiece was Jefferson's obsession."

corpus = {}
for i, sent in enumerate(sentences.split('\n')):
    corpus['sent{}'.format(i)] = dict((tok,1) for tok in sent.split())
df = pd.DataFrame.from_records(corpus).fillna(0).astype(int).T

df = df.T
print(df.sent0.dot(df.sent1))
print(df.sent0.dot(df.sent2))
print(df.sent0.dot(df.sent3))

print([(k, v) for (k, v) in (df.sent0 & df.sent3).items() if v])


#token improvement