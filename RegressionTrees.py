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
    def __init__(self, dataset, left=None, right=None,depth, splitfeature):
        self.left = left
        self.right = right
        self.dataset = dataset
        self.depth = depth
        self.splitfeature = splitfeature


# this function find the probability that a field is republican
#
def probability(field, party):
    return ((field[field['p'] == party]).count()/field.count())[0]

#purit: find the purity of a field using this logic
def purity(field):
    r = probability(field, 'republican')
    d = 1-r
    return (1 - (r*r) - (d*d))

def gini(field, splitCol):
    right = field[field[splitCol] == 'y']
    left =field[field[splitCol] != 'y']
    rightPurity = purity(right)
    leftPurity = purity(left)
    selfPurity = purity(field)
    return selfPurity - (rightPurity*rightPurity) - (leftPurity*leftPurity)

print gini(df,'0')
