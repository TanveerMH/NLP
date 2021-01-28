import os

fread = open("C:/recipe_Ital_102.txt","r")
f = fread.read()
print(f.split())
#words = f.split()
#print(words)

d ={}
for word in f.split():    
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

print(d)
               
    
