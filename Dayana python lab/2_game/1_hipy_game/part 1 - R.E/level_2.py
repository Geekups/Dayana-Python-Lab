# In the code below you have 3 ways to open and read a CSV file
# Primarily as a challenge to you
# Try to find and download a CSV file 
# containing data, such as the price of dollars or 
# bitcoins or whatever you want.
# Then put it next to this python file
# And exactly with the name data.csv 
# which is called in the code to the name of your downloaded file
# Execute all three parts of the following code separately. Write their differences
# Next, imagine yourself as a data scientist for a moment
# And analyze these 3 methods from your point of view
# And choose the best method by mentioning specific reasons
# Note: You must install the pandas library in your work environment
# The necessary instructions are available on the Internet
# Good luck!S
####################
import csv 
 
# opening the CSV file 
with open('data.csv', mode ='r')as file: 
 
 # reading the CSV file 
 csvFile = csv.reader(file) 
 
 # displaying the contents of the CSV file 
for lines in csvFile: 
    print(lines)
    
  ###################### v2 ########
  
import csv 
 
# opening the CSV file 
with open('data.csv', mode ='r')as file: 
 
 # reading the CSV file 
 csvFile = csv.DictReader(file) 
 
 # displaying the contents of the CSV file 
 for lines in csvFile: 
  print(lines)
 
 ############ v3 ##############
 
 import pandas 

 

# reading the CSV file 

csvFile = pandas.read_csv('data.csv') 

# displaying the contents of the CSV file 
print(csvFile)