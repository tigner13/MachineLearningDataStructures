""" Naive Bayes by Elizabeth Tigner
 I applied Bayes theorem to a data set on congressional votes.
 Naive Bayes is a type of supervised classification where it returns
 a probability that a certian person is of a policial party or not.
 The data I used was from:
 http://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records """

import pandas as pd
import numpy as np

df = pd.read_csv('house-votes-84.data')
class NaiveBayes(object):

    def __init__(self, file):
        self.file = file
        self.df = pd.read_csv(file)

    #deletes row if there is a NA
    def prob (self,party,i,vote):
        col = party[[i]]
        col = col[col[[0]] != '?']
        same = col[col[[0]] == vote]
        return (same.count() / col.count())[0]

    def bayes(self,person, party):
        billnum =1;
        p=1
        Party = df[df['p'] == party]
        for vote in person:
            pr = (self.prob(Party, billnum, vote))
            billnum +=1
            p = p*pr
        p = p * (Party.count() / df.count())[0]
        return p

    def party(self,person):
        republican = self.bayes(person, 'republican')
        democrat = self.bayes(person, 'democrat')
        if (republican > democrat): print "republican"
        else: print "democrat"

n='n'
y='y'
person = [n,n,y,n,n,y,n,y,n,y,y,n,n,n,y,y]
program = NaiveBayes('house-votes-84.data')
program.party(person)
