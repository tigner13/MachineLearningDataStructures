# Classification and Regression Trees (CART) are an applied application of
# recursion. We take a set of training data set and split it into a bunch of
# nested trees
#

import pandas as pd
import numpy as np
import sys

n='n'
y='y'
democrat = 'democrat'
republican = 'republican'

# importing data
df = pd.read_csv('house-votes-84-mini.data')

#building data structure for trees
class treeNode:
    def __init__(self, dataset, left, right, splitfeature,purity,party):
        self.dataset = dataset
        self.left = left
        self.right = right
        self.splitfeature = splitfeature
        self.purity = purity
        self.party=party


# this function find the probability that a field is republican
#
def probability(field, party):
    return ((field[field['p'] == party]).count()/field.count())[0]

#purity: find the purity of a field using this logic
def purity(field):
    if field.empty: return 1
    r = probability(field, 'republican')
    d = 1-r

    return  1 - (r*r) - (d*d)

def gini(field, col):
    right = field[field[col] == 'y']
    left =field[field[col] != 'y']
    rightPurity = purity(right)
    leftPurity = purity(left)
    selfPurity = purity(field)
    return selfPurity - (rightPurity*rightPurity) - (leftPurity*leftPurity)

def party(field):
    p = probability(field,'republican')
    if (p > .5): return 'republican'
    return 'democrat'

def split(field):
    p = purity(field)
    if(p < .24): return treeNode(field, None, None, None,p,party(field))
    maxGini = gini(field, '1')
    maxCol = '1'
    for column in df:
        g = gini(field,column)
        if (g > maxGini):
             maxGini = g
             maxCol = column
    return treeNode(field, split(field[field[maxCol] == 'y']), split(field[field[maxCol] != 'y']),maxCol,p,party(field))

def classify(person, node):
        while True:
            if person[int(node.splitfeature)] == 'y':
                node = node.left
            else:
                node = node.right
            if (node.right == None):
                break

        return node.party
def correct(person,node):
    party = person[0]
    person.pop(0)
    if(party == classify(person,node)): return 1
    else: return 0

#n = split(df)
#person = ['republican','n','y','n','y','y','y','n','n','n','n','n','n','y','y','n','y']
#print correct(person,n)


def printTree(node):
    if node == None: return
    print"\n"
    print node.dataset
    printTree(node.right)
    printTree(node.left)


##Testing purposes###
def efficiency(training, testing):
    training.columns = ['p','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    testing.columns = ['p','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    training = training.reset_index(drop=True)
    testing = testing.reset_index(drop=True)


    node = split(training)
    accuracy = 0
    rows = map(list,testing.values)
    for row in rows:
        c = correct(row, node)
        accuracy = accuracy + c

    return (float(accuracy)/float(len(testing)))

def kFoldTest(field, folds):
    df = field.reindex(np.random.permutation(field.index))
    average = 0
    p1 = 0;
    p2 = (len(df)/folds)

#test on trainingdata

#testing on the testing data sets
    for i in range(1,folds+1):
        if(i > 15): break
        if (p2 > len(df)): p2 = len(df)
        training = df[p1:p2]
        testing= df

        testing.drop(testing.index[p1:p2])

        traineff = efficiency(training, training)
        print "r ,", (p2-p1), ",", traineff
        if (traineff == 1): print training

        eff = efficiency(training,testing)
        #print "t ,",(p2-p1), ",",eff
        average += eff
        p1 += (len(df)/folds)
        p2 = p1 + (len(df)/folds)
    average = average/folds
    #print "t ,", (p2-p1), ",", average



kFoldTest(pd.read_csv('house-votes-84.data'), 20)
