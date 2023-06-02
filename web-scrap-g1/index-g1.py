import requests
from bs4 import BeautifulSoup
import pandas as pd


list_news = []

urlBase = 'https://g1.globo.com/'
response = requests.get(urlBase)

content = response.content

site =  BeautifulSoup(content, 'html.parser')

# HTML da noticia
news = site.findAll('div', attrs={'class': 'feed-post-body'})

for new in news:
    # titulo da noticia
    title = new.find('a', attrs={'class': 'feed-post-link'})
    subtitle = new.find('div', attrs={'class': 'feed-post-body-resumo'})
    linkPost = title['href']


    if (subtitle):
        list_news.append([title.text, subtitle.text, linkPost])
    else:
        list_news.append([title.text, '', linkPost])


resultNews = pd.DataFrame(list_news, columns=['Título', 'Subtítulo', 'Link'])
resultNews.to_excel('noticias.xlsx', index=False)
