from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
print(' '.join([stemmer.stem(w).strip("'") for w in "dish washer's washed dishes".split()]))