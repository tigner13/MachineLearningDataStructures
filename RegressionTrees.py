# Classification and Regression Trees (CART) are an applied application of
# recursionWe take a set of training data set and split it into a bunch of
# nested trees
#

import pandas as pd
import numpy as np

#importing data
df = pd.read_csv('house-votes-84.data')

#this function find the probability that a field is republican
#
def p(field):
    return (field[field['p'] == 'republican'].count() / field.count())[0]

# This is a function for the Gini measure of impurity.
# measures how often a randomly chosen element from a set would be incorectly
# labled.
# example of impurity: a set with all true/ a set with all false
# equation: G(t) = 1- p(t)^2 - (1 - p(t))^2
def g(field):
     return (1 - (p(field)*p(field)) - ((1 -  p(field))*(1 - p(field))))
