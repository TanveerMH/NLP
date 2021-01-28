# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:40:12 2020

@author: Hasan Tanveer Mahmood 1725413

"""

import os
os.chdir('F:/SEM 05/NATURAL LANGUAGE PROCESSING/EXERCISE/Exercise 2')

def find_word(filename):
    dd=[]
    for word in filename.split():
        if word.endswith("ly"):
            dd.append(word)
    return dd
 
    

def countOf():
    fl = open('recipe_Ital_115.txt','r')
    count = 0
    data = fl.read()
    wrd = data.split()
    for i in wrd:
        if i =='of':
            count+=1
    return count      
    fl.close()
   
with open("recipe_Ital_115.txt") as f:
    f = f.read()

d ={}
for word in f.split():    
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1


filename = open("results.txt",'w')
filename.write("Frequency of unique words:\n" + str(d) + "\n")
filename.write("There is  : "+ str(countOf())+" 'of'\n")
filename.write("Words ending with 'ly': " + str(find_word(f)) + "\n")
filename.close()

print("\nFrequency of unique words:\n" + str(d) + "\n")
print("Words ending with 'ly': " + str(find_word(f)) + "\n")
print("There is  : "+ str(countOf())+" 'of'\n")
