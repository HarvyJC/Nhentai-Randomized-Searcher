import random, requests, time, webbrowser
from bs4 import BeautifulSoup as bs

r = requests.get('https://nhentai.net')
soup = bs(r.content, 'html.parser')

divtag = soup.find_all('div', class_="container index-container")

for tag in divtag:
    a = tag.find_all('a', class_='cover', href=True)

    for i in a[:1]:
        text = i['href']
        set0 = text

set1 = set0.replace('/g/', '')
set2 = set1.replace('/','')

#webbrowser.register('firefox',
#	None,
#	webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))

print('Nhentai Doujin Searcher V1\n   By Harold Cabungcal')
print('Please note this does not YET open the links in incognito mode.')
max = int(input('Max Pages to Search: '))

for i in range(max):
    val = random.randint(000000, int(set2))
    url = 'https://nhentai.net/g/' + str(val)
    print(url)
    #webbrowser.get('firefox').open_new(url)
    webbrowser.open(url)
    time.sleep(1)