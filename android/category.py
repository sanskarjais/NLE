import json
import os

with open('data.json', 'r') as fjson:
    data = json.load(fjson)

Choice = []
for i in data:
    new = []
    new.append(i)
    new.append(i)
    Choice.append(tuple(new))
Choice = tuple(Choice) 
# print(Choice)