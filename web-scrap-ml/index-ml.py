import requests
from bs4 import BeautifulSoup
import pandas as pd

urlBase = 'https://lista.mercadolivre.com.br/'
produto = input('Digite o produto? ')
response = requests.get(urlBase + produto)

print(urlBase + produto)
#content = response.content

#site = BeautifulSoup(content, 'html.parser')

#print(site.prettify())