# Classification and Regression Trees (CART) are an applied application of
# recursion. We take a set of training data set and split it into a bunch of
# nested trees
#

import pandas as pd
import numpy as np

# importing data
df = pd.read_csv('house-votes-84-mini.data')

#building data structure for trees
class treeNode:
    def __init__(self, dataset, left, right, splitfeature,purity):
        self.dataset = dataset
        self.left = left
        self.right = right
        self.splitfeature = splitfeature
        self.purity = purity


# this function find the probability that a field is republican
#
def probability(field, party):
    return ((field[field['p'] == party]).count()/field.count())[0]

#purity: find the purity of a field using this logic
def purity(field):
    if field.empty: return 1
    r = probability(field, 'republican')
    d = 1-r
    return (1 - (r*r) - (d*d))

def gini(field, col):
    right = field[field[col] == 'y']
    left =field[field[col] != 'y']
    rightPurity = purity(right)
    leftPurity = purity(left)
    selfPurity = purity(field)
    return selfPurity - (rightPurity*rightPurity) - (leftPurity*leftPurity)

def split(field):
    p = purity(field)
    if(p == 0): return treeNode(field, None, None, None,p)
    maxGini = gini(field, '1')
    maxCol = '1'
    for column in df:
        g = gini(field,column)
        if (g > maxGini):
             maxGini = g
             maxCol = column
    return treeNode(field, split(field[field[maxCol] == 'y']), split(field[field[maxCol] != 'y']),maxCol,p)

def classify(person, field):
        node = split(df)
        print (node.splitfeature)

        while True:
            if person[int(node.splitfeature)] == 'y':
                node = node.left
            else:
                node = node.right
            if (node.right == None):
                break
        print node.dataset['p']

person = ['y','y','y','n','y','y','n','n','n','n','y','n','y','y','y','y']
classify(person,df)
