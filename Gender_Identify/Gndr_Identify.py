'''
Jaki Fayek Alvi Rahman - 1721485
Hasan Tanveer Mahmood - 1725413
'''
import nltk
from nltk.corpus import names   

def gender_features(name):
    return {'last_letter':name[-1]}

labeled_names = ([(name,'male') for name in names.words('jap_male.txt')] + [(name,'female') for name in names.words('jap_female.txt')])
import random
random.shuffle(labeled_names)
#print(labeled_names)

featureSets = [(gender_features(n),gender) for (n,gender) in labeled_names]
train_set, test_set = featureSets[70:],featureSets[:30]
classifier = nltk.NaiveBayesClassifier.train(train_set)

name = input('Enter a Japanse Name: ')
print(name,'is',classifier.classify(gender_features(name)))
print('Accuracy: ',nltk.classify.accuracy(classifier,test_set))
print(classifier.show_most_informative_features(5))
