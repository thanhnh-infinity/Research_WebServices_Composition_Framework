import nltk
import string
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

#nltk.download('punkt')
stemmer = PorterStemmer()

def preprocessing(text):
    lowers = text.lower()
    no_punctuation = lowers.translate(None, string.punctuation)
    return no_punctuation

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

def getSim_btw_2_descriptions(des_1, des_2):
    #data = tokenize(des_2)
    #for item in data:
    #    print item
    #print des_1
    #print des_2
    vect  = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfidf = vect.fit_transform([preprocessing(des_1),preprocessing(des_2)])
    #print tfidf
    pairwise_similarity = (tfidf * tfidf.T).A
    print pairwise_similarity
    return pairwise_similarity[0][1]