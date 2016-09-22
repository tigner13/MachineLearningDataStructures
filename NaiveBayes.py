import pandas as pd
import numpy as np

df = pd.read_csv('house-votes-84.data')

#deletes row if there is a NA
def prob (party,i,c):
    col = party[[i]]
    col = col[col[[0]] != '?']
    yes = col[col[[0]] == c]
    return yes.count() / col.count()

Republican = df[df['p'] == 'republican']
probR = Republican.count() /  df.count()
person = ['y','y','y','n','y','y','n','n','n','n','y','n','y','y','y','y']
p = 1;
bilnum = 1
for vote in person:
    p = p * prob(Republican, bilnum, vote)
    bilnum +=1

print p
