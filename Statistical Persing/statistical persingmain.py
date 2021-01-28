# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:20:52 2021

@author: Prince
"""

import nltk
from nltk.draw.tree import draw_trees
from nltk.parse import pchart
grammer = nltk.PCFG.fromstring("""
                               S -> NP VP [0.8] | Aux NP VP [0.1] | VP [0.1]
                               NP -> Det Nominal [0.6] | Pronoun [0.2] | Proper-Noun [0.2]
                               Nominal -> Noun [0.3] | Nominal Noun [0.2] | Nomial PP [0.5]
                               VP -> Verb [0.3] | Verb NP [0.2] | VP PP [0.5]
                               PP -> Prep NP [1.0]
                               Det -> 'the' [0.6] | 'a' [0.2] | 'that' [0.1] | 'is' [0.1]
                               Verb -> 'book' [0.5] | 'include' [0.2] | 'prefer' [0.3]
                               Noun -> 'book' [0.1] | 'flight' [0.5] | 'meal' [0.2] | 'money' [0.2]
                               Proper-Noun -> 'Houston' [0.8] | 'NWA' [0.2]
                               Prep -> 'from' [0.25] |'to' [0.25] | 'near' [0.1] | 'through' [0.2] | 'on' [0.2]
                               """)

print(grammer)
parser = pchart.InsideChartParser(grammer)

sent = "book the flight through Houston"

trees = parser.parse(sent.split())

for t in trees:
    print(t)
    draw_trees(t)

    