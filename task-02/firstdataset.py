from bs4 import BeautifulSoup
from urllib.request import urlopen 

url = urlopen("https://catalog.data.gov/dataset?q=&sort=metadata_created+desc") 
soup = BeautifulSoup(url.read(), 'html.parser')


for hit in soup(attrs={'href' : '/dataset/series-information-file-for-the-2017-tiger-line-shapefile-area-hydrography-county-based-shapefi'}):
    hit = hit.getText()  
    print((hit))