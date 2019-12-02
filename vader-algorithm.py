from vaderSentiment.vaderSentiment import SentimentIntensityAnalyser
sa = SentimentIntensityAnalyser()
sa.lexicon

corpus = ["Absolutely perfect! Love it! :-) :-) :-)",
"Horrible! Completely useless. :(",
"It was OK. Some good and some bad things."]
for doc in corpus:
    scores = sa.polarity_scores(doc)
    print('{:+}: {}'.format(scores['compound'], doc))