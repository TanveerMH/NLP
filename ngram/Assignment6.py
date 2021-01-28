# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:07:20 2020

@author: Hasan Tanveer Mahmood 1725413

"""

import re
import os
os.chdir("F:/SEM 05/NATURAL LANGUAGE PROCESSING/EXERCISE/Exercise 6/ngram")

def ngram():
    #Given Sentence
    sent = "Most mental disorders can is treatable through early detection of signs or symptoms"
   
    no_of_time_bi = {}
    no_of_time_uni = {}
    no_of_time_test= {}
    
    #spiling the sentence or tokenizing
    for words in range(len(sent.split())-1):
        text = (sent.split()[words]+" "+sent.split()[words+1]).casefold()
        if text not in no_of_time_test:
            no_of_time_test[text] = 1
        else:
            no_of_time_test[text] += 1
            
    #using "with" will close the file immediately after last call
    with open("text-ngram.dat","r") as rfile:
        infile = rfile.readlines()

    unifile = open("unigram.dat","w")
    bifile = open("bigram.dat","w") 
    trifile = open("trigram.dat","w")   
    
    sent2 = [s for s in infile[0].split(".")]
    
   #spiling the sentence 2 or tokenizing
    for line in sent2:        
        for x in range(len(line.split())-1):
            uni = (line.split()[x]).casefold()
            if uni not in no_of_time_uni:
                no_of_time_uni[uni] = 1
            else:
                no_of_time_uni[uni] += 1
                
            bi = (line.split()[x]+" "+line.split()[x+1]).casefold()
            if bi not in no_of_time_bi:
                no_of_time_bi[bi] = 1
            else:
                no_of_time_bi[bi] += 1
            #write into the file     
            unifile = open("unigram.dat","a")
            bifile = open("bigram.dat","a")            
            unifile.write(str(uni)+"\n")
            bifile.write(str(bi)+"\n")            
            unifile.close()
            bifile.close()
            
        for k in range(len(line.split())-2):
            trifile = open("trigram.dat","a")            
            tri = line.split()[k]+" "+line.split()[k+1]+" "+line.split()[k+2]
            trifile.write(str(tri)+"\n")
            trifile.close()
              
    #probability of each bigram
    prob = []
    for y in no_of_time_test:
        if y not in no_of_time_bi:
            prob.append(0)
        else:
            prob.append(no_of_time_bi[y]/no_of_time_uni[y.split()[0]])
    
    #probability of whole sentence
    wProb = 1        
    for i in prob:
        wProb *= i
     
    print("\nBigram: ",no_of_time_bi)
    print("\n\nUnigram: ",no_of_time_uni)
    print("\n\nTesting:  ",no_of_time_test)
    print("\n\nProbability of each bigram in testing sentence: ",prob)
    print("\nProbability of the whole sentence: ",wProb)
    
#Function Calling   
ngram()

