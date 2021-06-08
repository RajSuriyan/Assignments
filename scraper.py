from bs4 import BeautifulSoup
import requests
 

source = requests.get('https://www.healthline.com/health/coronavirus-covid-19').text
soup = BeautifulSoup(source,'lxml')

match = soup.prettify()

print(match)
