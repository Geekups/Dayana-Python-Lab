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