'''
Created on 04.09.2014

@author: proSingularity
'''

COLORS_TO_NUMBERS = {
          "blue": 1,
          "red": 2,
          "yellow": 3,
          "brown": 4,
          "green": 5,
          "orange": 6,
          }

# the number of stones per combination
CODELENGTH = 3

# number of rounds played
ROUND_NUMBER = 4

DEBUG_LEVEL = 2

NUMBERS_TO_COLORS = {v: k for k, v in COLORS_TO_NUMBERS.iteritems()}
