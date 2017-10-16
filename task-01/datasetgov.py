#coding: utf-8

from bs4 import BeautifulSoup
from urllib.request import urlopen

datagov = urlopen("https://catalog.data.gov/dataset")
bsObj = BeautifulSoup(datagov.read(), 'html.parser')
datasetNumber = bsObj.findAll("<!-- Snippet snippets/search_result_text.html start -->", "<!-- Snippet snippets/search_result_text.html end -->")

for hit in bsObj(attrs={'class' : 'new-results'}):
    numbers = hit.getText().replace("\n", "")
    
print(numbers[8:15])
