""" Naive Bayes by Elizabeth Tigner
 I applied Bayes theorem to a data set on congressional votes.
 Naive Bayes is a type of supervised classification where it returns
 a probability that a certian person is of a policial party or not.
 The data I used was from:
 http://archive.ics.uci.edu/ml/datasets/Congressional+Voting+Records """

import pandas as pd
import numpy as np

"""global variables"""
n='n'
y='y'
democrat = 'democrat'
republican = 'republican'

class NaiveBayes(object):
    '''
    Function Discription:
    intializer of NaiveBayes Bayes
    Inputs
    base: a fd of the base peole we are running our tests off
    test: a df of the the people we are testing
    '''
    def __init__(self, base, test):
        self.base = base
        self.test = test

    '''
    Function Discription:
    Inputs
    party: a subset of the origional dataframe in which it only includes the
    members of the "party" party
    i: the bill number you are anzalyzing
    vote: if the person you are analyzing voted yes or no on the bill

    Output: the probability that the person is in the party given their vote
    '''
    def prob (self,party,i,vote):
        col = party[[i]]
        col = col[col[[0]] != '?']
        same = col[col[[0]] == vote]
        return (same.count() / col.count())[0]


    '''
    Function Discription:
    Inputs
    person: a list of all the votes of the peron your are analyzing
    party: a string that repreents what party you are analyzing

    Output
    the probability that the person is in the party given all their votes
    '''
    def bayes(self,person, party):
        billnum =1;
        p=1
        Party = base[base['p'] == party]
        for vote in person:
            pr = (self.prob(Party, billnum, vote))
            billnum +=1
            p = p*pr
        p = p * (Party.count() / base.count())[0]
        return p

    '''
    Function Discription:
    Inputs
    person: a list  of the votes of person you are analyzing

    Output
    The prediction if it is a republican or democrat
    '''
    def prediction(self,person):
        republican = self.bayes(person, 'republican')
        democrat = self.bayes(person, 'democrat')
        if (republican > democrat): return 'republican'
        else: return 'democrat'

    '''
    Inputs
    person: a list of all atributes of the person you are analyzing

    Output
    1: if the program accuratly predict the person
    0: if the program didn't accuratly predict the person
    '''
    def corect(self, person):
        party = person[0]
        person.pop(0)
        if(party == self.prediction(person)): return 1
        else: return 0

    """
    This function find the accuracy of the program
    """
    def efficiency(self):
        num = 0
        for row in self.test.row:
            num = num + self.corect(row)
        return (num/len(self.test))


def kFoldSplit(df, folds):
    array = np.array_split(df,100)
    dfarray = []
    p1 = 0;
    p2 = (len(df)/folds)
    for i in range(1,folds+1):
        if (p2 > len(df)): p2 = len(df)
        dfarray.append(df[p1:p2])
        p1 += (len(df)/folds)
        p2 = p1 + (len(df)/folds)
    print dfarray[folds-1]



person = [democrat,n,n,y,n,n,y,n,y,n,y,y,n,n,n,y,y]
kFoldSplit(pd.read_csv('house-votes-84.data'), 4)
