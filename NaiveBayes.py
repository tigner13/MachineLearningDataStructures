# Naive Bayes by Elizabeth Tigner
# I applied Bayes theorem to a data set on congressional votes.
# Naive Bayes is a type of supervised classification where it returns
# a probability that a certian person is of a policial party or not.
# The data I used was from:
# http://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records

import pandas as pd
import numpy as np

df = pd.read_csv('house-votes-84.data')


#deletes row if there is a NA
def prob (party,i,vote):
    col = party[[i]]
    col = col[col[[0]] != '?']
    same = col[col[[0]] == vote]
    return (same.count() / col.count())[0]

def bayes(person, party):
    billnum =1;
    p=1
    Party = df[df['p'] == party]
    for vote in person:
        (prob(Party, billnum, vote))
        billnum +=1
    p = p* (Party.count() / df.count())[0]
    return p



person = ['n','y','y','y','y','y','n','n','n','y','y','n','y','y','n','n']
print bayes(person, 'republican') / (bayes(person, 'democrat') + bayes(person, 'republican'))
