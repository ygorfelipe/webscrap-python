import requests
from bs4 import BeautifulSoup
import pandas as pd

urlBase = 'https://lista.mercadolivre.com.br/'
# produto = input('Digite o produto? ')

# response = requests.get(urlBase + produto)
response = requests.get(urlBase + 'iphone')
site =  BeautifulSoup(response.text, 'html.parser')

productCard = site.find('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default'})

print(productCard.prettify())

# for product in productCard:

#     titleProduct = productCard.find('h2', attrs={'class': 'ui-search-item__title'})
#     linkProduct = productCard.find('a', attrs={'class': 'ui-search-link'})
#     priceFraction = productCard.find('span', attrs={'class': 'price-tag-fraction'})
#     priceCents = productCard.find('span', attrs={'class': 'price-tag-cents'})

#     # #print(productCard.prettify())
#     # if (titleProduct):
#     #     print(f'ProductName: {titleProduct.text}')
#     # if (priceCents):
#     #     print(f'PriceProduct: R$: {priceFraction.text},{priceCents.text}')
#     # print(linkProduct['href'])
#     # print('\n\n')


    #produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

# for produto in produtos:
#     titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
#     link = produto.find('a', attrs={'class': 'ui-search-link'})

#     real = produto.find('span', attrs={'class': 'price-tag-fraction'})
#     centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

#     print(produto.prettify())
#     print('Título do produto:', titulo.text)
#     print('Link do produto:', link['href'])

#     if (centavos):
#         print('Preço do produto: R$', real.text + ',' + centavos.text)
#     else:
#         print('Preço do produto: R$', real.text)
    
#     print('\n\n')
#     break


