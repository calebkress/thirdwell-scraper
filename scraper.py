import os
import requests
from BeautifulSoup import BeautifulSoup

def getText(url=raw_input('Enter URL: ')):
    response = requests.get(url)
    html = response.content

    resultArr = []
    soup = BeautifulSoup(html)
    for p in soup.findAll('p'):
        resultArr.append(p.text.replace('\n', ' ').replace('\\', ' ').replace('&#xa0;', ' '))
    result = ' '.join(resultArr)

    title = url.split('/').pop()
    if not os.path.exists('./text-files/' + title.replace('.html', '.txt')):
        with open('./text-files/' + title.replace('.html', '.txt'), 'w') as file:
            file.write(title.replace('.html', '').replace('-', ' ') + '\n' + result)
    else:
        with open('./text-files/' + title.replace('.html', '.txt'), 'w') as file:
            file.write(title.replace('.html', '').replace('-', ' ') + '\n' + result)

    return result

print getText()
