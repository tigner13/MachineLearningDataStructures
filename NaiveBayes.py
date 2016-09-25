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
