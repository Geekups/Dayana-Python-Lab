# snippet for working with xml

import xml.etree.ElementTree as ET 

# Pass the path of the xml document 

tree = ET.parse('sample_CustomersOrders.xml') 

# get the parent tag 

root = tree.getroot() 

# print the root (parent) tag along with its memory location 

print(root) 

# print the attributes of the first tag 

print(root[0].attrib)

######################

# snippet to work with json
import json

# Opening JSON file 

json_data = open('data.json').read()

# returns JSON object as 

# a dictionary 

data = json.loads(json_data)

# Iterating through the json 

# list 

for item in data: 

 print (item)