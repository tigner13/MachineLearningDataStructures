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
    def __init__(self,left, right,dataset):
        self.left = left
        self.right = right
        self.dataset = dataset


# this function find the probability that a field is republican
#
def p(field):
    return ((field[field['p'] == 'republican']).count()/field.count())[0]

# This is a function for the Gini measure of impurity.
# measures how often a randomly chosen element from a set would be incorectly
# labled.
# example of impurity: a set with all true/ a set with all false
# equation: G(t) = 1- p(t)^2 - (1 - p(t))^2
def gini(field):
    return (1 - (p(field)*p(field)) - ((1 -  p(field))*(1 - p(field))))


#This choses what collumn to split at by using gini
def split(field):
    splitCol = list(field)[1]
    for column in field:
        if (gini(field[field[column] == 'y']) < gini(field[field[splitCol] == 'y'])):
            splitCol = column
    return splitCol

# this function is constructing the tree
#current problem is that it is spliting at the smae node everytime
def construct(field):
     if((field.count()[0] == 1) or (field.count()[0] == 0) or p(field) == 1):
         return field
     else:
         splitC = split(field)
         L = field[field[splitC] == 'y']
         L =L.drop(splitC,axis=1)
         R = field[field[split(field)] != 'y']
         R = R.drop(splitC,axis=1)
         return treeNode(construct(L),construct(R),field)

def printTree(root):
    level = root
    while level:
        nextLevel = list()
        if (level != root):
            for n in level:
                print n.dataset
                if n.left: nextLevel.append(n.left)
                if not(n.right).empty: nextLevel.append(n.right)
        else:
            print level.dataset
            if level.left: nextLevel.append(level.left)
            if level.right: nextLevel.append(level.right)
        print
        level = nextLevel

printTree(construct(df))
