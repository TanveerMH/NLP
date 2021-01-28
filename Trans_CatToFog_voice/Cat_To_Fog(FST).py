# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 22:53:17 2020

@author: Hasan Tanveer Mahmood 1725413
         Jaki Fayek Alvi Rahman 1721485
"""


from nltk.nltk_contrib.fst.fst import *

class myFST(FST):
    def recognize(self, iput, oput):
        self.inp = list(iput)
        self.outp = list(oput)
        
        if list(oput) == f.transduce(list(iput)):
           
            return True
        else:
            return False

f = myFST('example')
for i in range(1, 7):
    f.add_state(str(i))

f.initial_state = '1'  

f.add_arc('1', '2', ('m'), ('o')) 
f.add_arc('2', '3', ('e'), ('i'))  
f.add_arc('3', '4', ('o'), ('n'))  
f.add_arc('4', '5', ('w'), ('k'))  
f.add_arc('5', '6', ('!'), ('!'))  
f.add_arc('6', '1', (),())  

f.set_final('6')

inp = "meow!"
outp = "oink!"
print(inp)

if f.recognize(inp, outp):
    print(outp)
    print("accept")
else:
    print("reject")

disp = FSTDisplay(f)