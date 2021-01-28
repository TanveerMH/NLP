# -- coding: utf-8 --
"""
Created on Sat Dec 26 8:16:00 2020

@author: Hasan Tanveer Mahmood 1725413
        Jaki Fayek Alvi Rahman 1721485
"""

import nltk
import string
import os
import math
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

os.chdir("F:/SEM 05/NATURAL LANGUAGE PROCESSING/CODE FROM TEACHER/Topics6")
term = ["fail", "dollar", "match", "trade", "survivor"] 

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def get_tokens(file):
    with open(file, 'r', encoding='utf-8', errors='ignore') as article:
        text = article.read()
        lowers = text.lower()
        no_punctuation = lowers.translate(string.punctuation)
        tokens = nltk.word_tokenize(no_punctuation)
        return tokens
    
def calc_tf(w):
    tf = []
    file = ['art1.dat', 'art2.dat', 'art3.dat', 'art4.dat', 'art5.dat', 'art6.dat']
    for f in file:
        tokens = get_tokens(f)
        filtered = [w for w in tokens if not w in stopwords.words('english')]
        stemmer = PorterStemmer()
        stemmed = stem_tokens(filtered, stemmer)
        count = Counter(stemmed)
        tf.append(count[w]/len(stemmed))
    return tf 

def calc_idf(tf):
    idf = 0
    for i in tf:
        if i>0:
            idf = idf + 1
    return math.log(6/idf)    

def calc_tf_idf(tf, idf):
    tfidf = []
    for i in tf:
        tfidf.append(i*idf)
    return tfidf

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

def k_means(tfs):
    true_k = 2
    model = KMeans(n_clusters = true_k, init='k-means++', max_iter=50, n_init=1)
    model.fit(tfs)
    print('Top terms per cluster:')
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = tfidf.get_feature_names()
    
    for i in range(true_k):
        print("\nCluster %d: " % i)
        for ind in order_centroids[i, :10]:
            print('%s' % terms[ind])
            
term = ["fail", "dollar", "match", "trade", "survivor"]           

for terms in term:
    tf = calc_tf(terms)
    idf = calc_idf(tf)
    tfidf = calc_tf_idf(tf,idf)
    print(f"tf of term '{terms}':- \n-------------------------------------------------------")
    for i in range(len(tf)):
        print(f"art {i+1}: '{terms}' = {tf[i]}")
    
    print(f"\nidf('{terms}') = {idf}")
    
    print(f"tf-idf of term '{terms}':- \n-------------------------------------------------------")
    for i in range(len(tf)):
        print(f"art {i+1}: '{terms}' = {tfidf[i]}")
     
    print('\n')