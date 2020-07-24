 #-*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:19:03 2020

@author: anilc
"""

def konubul(metin):
    import os
    yol = os.path.dirname(os.path.realpath(__file__))
    import pandas as pd 
    data = pd.read_csv(yol+"\\"+"dataset.txt", engine='python')
    sentences_training = [doc for doc in data.iloc[:,0]]
    classification_training = [doc for doc in data.iloc[:,1]]
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer(analyzer='word', lowercase = True)
    sen_train_vector = vectorizer.fit_transform(sentences_training)
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    model = clf.fit(X=sen_train_vector.toarray(), y=classification_training)
    sen_test_vector = vectorizer.transform([metin]) 
    y_pred = model.predict(sen_test_vector.toarray())
    if y_pred == 1: 
        return "futbol "

    elif y_pred == 0:
        return "siyaset"

    else:
        return "Hata aldım"
 
