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


'''
Function Discription:
Inputs
party: a subset of the origional dataframe in which it only includes the
members of the "party" party
i: the bill number you are anzalyzing
vote: if the person you are analyzing voted yes or no on the bill

Output: the probability that the person is in the party given their vote
'''
def prob (party,i,vote):
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
def bayes(data,person, party):
    billnum =1;
    p=1
    Party = data[data['p'] == party]
    for vote in person:
        pr = (prob(Party, billnum, vote))
        billnum +=1
        p = p*pr
    p = p * (Party.count() / data.count())[0]
    return p

'''
Function Discription:
Inputs
person: a list  of the votes of person you are analyzing

Output
The prediction if it is a republican or democrat
'''
def prediction(data, person):
    republican = bayes(data, person, 'republican')
    democrat = bayes(data, person, 'democrat')
    if (republican > democrat): return 'republican'
    else: return 'democrat'

'''
Inputs
person: a list of all atributes of the person you are analyzing
    Output
    1: if the program accuratly predict the person
    0: if the program didn't accuratly predict the person
'''
def corect(data, person):
    party = person[0]
    person.pop(0)
    if(party == prediction(data, person)): return 1
    else: return 0
    """
This function find the accuracy of the program
"""
def efficiency(testing, training):
    training.columns = ['p','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    testing.columns = ['p','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    training = training.reset_index(drop=True)
    testing = testing.reset_index(drop=True)

    num = 0
    rows = map(list,testing.values)

    for row in rows:
        num = num + corect(testing, row)
    return (float(num)/float(len(testing)))

"""
This folds the df in to f pieces
"""
def kFoldTest(field, folds):
    df = field.reindex(np.random.permutation(field.index))
    average = 0
    p1 = 0;
    p2 = (len(df)/folds)

    for i in range(1,folds+1):

        if (p2 > len(df)): p2 = len(df)
        training = df[p1:p2]
        testing= df
        testing.drop(testing.index[p1:p2])

        eff = efficiency(training,testing)
        print (p2-p1), ",",eff
        average += eff
        p1 += (len(df)/folds)
        p2 = p1 + (len(df)/folds)
    average = average/folds
    print (p2-p1), ",", average

df = pd.read_csv('house-votes-84.data')


for i in range(2,20):
    kFoldTest(df, i)
