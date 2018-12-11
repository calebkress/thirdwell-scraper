import os
import requests
from BeautifulSoup import BeautifulSoup

def getText(url=raw_input('Enter URL: ')):
    title = url.split('/').pop()
    if not os.path.exists('./text-files/' + title):
        with open('./text-files/' + title, 'w'): pass

    response = requests.get(url)
    html = response.content

    resultArr = []
    soup = BeautifulSoup(html)
    for p in soup.findAll('p'):
        resultArr.append(p.text.replace('\n', ' ').replace('\\', ' ').replace('&#xa0;', ' '))

    return ' '.join(resultArr)

print getText()
