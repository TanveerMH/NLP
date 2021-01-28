# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:58:04 2020

@author: Hasan Tanveer Mahmood 1725413
"""

import os
os.chdir("F:/SEM 05/NATURAL LANGUAGE PROCESSING/EXAMS/Test 1 part 3/")
from typing import Optional, Any

import nltk
import pickle
import re

# Read data from the file

with open("emails.dat", 'r') as file:
	file_content = file.read()



# Split the content by lines and tabs
file_content_splitted = [text.strip().split('\t') for text in file_content.splitlines()];

file_content_array = []
#creating an empty array

# Loop through the file_content_splitted to make all content in 1D array
for line in file_content_splitted:
	for content in line:
		file_content_array.append(content)

# regex for matching all date and number
dates = re.findall(r"[\d]{1,2}.[a-zA-Z] [ADFJMNOS]\w* [\d]{4}", file_content)
phone = re.findall(r'[\+\(]?[0-9][0-9 .\-\(\)]{8,}[0-9]', file_content)


# displaying all date in the file
print("Dates\n")
for date in dates:
	print(date)

# displaying all phone number in the file
print("Phone Number\n")
for number in phone:
	print(number)



