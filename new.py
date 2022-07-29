import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://squirrel-news.net/news/')
soup = BeautifulSoup(page.content, 'html.parser')
# print (soup.prettify())
data = soup.find('div', attrs = {'class':'wpcap-grid'})
sp_data=data.find('div',attrs={'class':'wpcap-grid-container elementor-grid wpcap-grid-desktop-2 wpcap-grid-tablet-2 wpcap-grid-mobile-1'})
fdata=sp_data.find_all('div',attrs={'class':'post-grid-thumbnail'})
imgs=[]
links=[]
headings=[]
for item in fdata:
    x=item.find('img')
    y=item.find('a')
    imgs.append(x['src'])
    links.append(y['href'])
# print(len(imgs))
# print(len(links))
ndata=sp_data.find_all('div',attrs={'class':'post-grid-text-wrap'})
for item in ndata:
    headings.append(item.a.text)

with open('result.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    data = list(zip(headings, imgs, links))
    for row in data:
        row = list(row)
        spamwriter.writerow(row)
print("Program completed")









