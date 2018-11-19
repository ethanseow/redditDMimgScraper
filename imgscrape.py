from linkscrape import redditScrape
from bs4 import BeautifulSoup, SoupStrainer
import urllib, urllib.request, time, json

def imgScrape(maxNum):
    linkList = redditScrape(maxNum)
    errors = 0
    imgList = []
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'

    for link in linkList:
        try:
            req = urllib.request.Request(link, headers= headers)
            respData = urllib.request.urlopen(req)
        except:
            continue
        else:
            strainer = SoupStrainer('img')
            parser = BeautifulSoup(respData.read(), parse_only = strainer, features = 'lxml')
            try:
                img = parser.find('img', class_ = '_2_tDEnGMLxpM6uOa2kaDB3 media-element')['src']
                imgList.append(img)
            except Exception as e:
                errors += 1
    with open('C:\\Users\\eths6\\Desktop\\PythonProjects\\memes.txt', 'a') as file:
        file.seek(0)
        file.truncate()
        for e in imgList:
            file.write(e)
            file.write('\n')

imgScrape(3)
"""
t1 = time.time()
print('working')
print(imgScrape(200))
print('Length of list is :{}'.format(imgList.len()))
t2 = time.time() - t1
print(t2)
"""

