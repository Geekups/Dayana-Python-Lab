# This simple code is made for short and static work
# From the following two libraries to get the content of a page
# And then we checked and extracted specific items from that content
# Your task at this stage is very easy.
# First, read the code and then write the steps to write it in order
# And finally, any kind of problem you see in the code
# Or write any improvement method you have in mind in the continuation of your analysis
# Put the number and name of the step at the bottom of the page and go to the next step
# Make sure that the content he writes is in the form of a file
# pdf or txt  
import requests
from bs4 import BeautifulSoup
 
request =requests.get('https://en.m.wikipedia.org/wiki/Machine_learning')

page_content = request.content

soup = BeautifulSoup(page_content, features="html.parser")

for element in soup.findAll('p'):
    print(element.text)
    