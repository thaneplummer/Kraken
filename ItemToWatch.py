import os
import re

filepath = r"C:\Projects\Kraken\CmdThreat\ClientDevelopment\UIPolicies"
itw = r"\ItemToWatch-"
with open(r"C:\Users\randy\Documents\Programming_resources\Scripts\Python_Scripts\itemtowatch.txt", 'r') as f:
    itwModel = f.read() 

def makeFileName(field):
    words = [i.title() if not i.isupper() else i for i in field.split()]
    name = ''.join(words)
    return name

def makeItw(field):
    fName = makeFileName(field)
    fileName = filepath+itw+fName+".txt"
    fieldkey = re.compile(r'\(itw\)')
    fieldFile = re.compile(r'\(itwF\)')
    
    with open(fileName, 'w') as f:
        data = fieldkey.sub(field, itwModel)
        data = fieldFile.sub(fName, data)
        f.write(data)

fields = ['CMDB Group', 'Connection', 'Incident', 'MSL log', 'Other', 'Problem']
for field in fields:
    makeItw(field)