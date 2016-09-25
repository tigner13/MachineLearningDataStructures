import pandas as pd
import numpy as np

df = pd.read_csv('house-votes-84.data')


#deletes row if there is a NA
def prob (party,i,c):
    col = party[[i]]
    col = col[col[[0]] != '?']
    yes = col[col[[0]] == 'y']
    return (yes.count() / col.count())[0]

def bayes(person, party):
    billnum =1;
    p=1
    Party = df[df['p'] == party]
    for vote in person:
        p *= (prob(Party, billnum, vote))
        billnum +=1
    print p
    p *= (Party.count() / df.count())[0]
    print p



person = ['y','y','y','n','y','y','n','n','n','n','y','n','y','y','y','y']
bayes(person, 'democrat')
