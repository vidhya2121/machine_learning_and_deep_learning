# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:45:44 2021

@author: vidhya
"""
import os
import io
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def read_files(path):
    print(path)
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)
            inbody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inbody:
                    lines.append(line)
                elif line == '\n':
                    inbody = True
            f.close()
            message = '\n'.join(lines)
            print(message)
            yield path, message

def data_frame_from_directory(path, classification):
    rows = []
    index = []
    for filename, message in read_files(path):
        rows.append({'message':message, 'class':classification})
        index.append(filename)
    return DataFrame(rows, index=index)

data = DataFrame({'message':[], 'class':[]})
data = data.append(data_frame_from_directory('emails/ham', 'ham'))
data = data.append(data_frame_from_directory('emails/spam', 'spam'))

print(data.head())

vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)

classifier = MultinomialNB()
targets = data['class'].values

classifier.fit(counts, targets)

examples = ['Aree you free tomorrow', "Free Discount Win 1 million dollar"]
example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)
print('predisctions: ', predictions)
