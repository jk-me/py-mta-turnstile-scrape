import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = "http://web.mta.info/developers/turnstile.html"
response = requests.get(url)
print('resp', response)

soup = BeautifulSoup(response.text, "html.parser")
# print('soup', soup)

# see all <a> tags, print in terminal with index to see which are useful (from 36 on)
# soup.findAll('a')
# for i in range (0, len(soup.findAll('a'))):
#     print(i, soup.findAll('a')[i])

#capture href from an <a> tag
one_a_tag = soup.findAll('a')[36]
print( 'one_a', one_a_tag)
link = one_a_tag['href']  #'data/nyct/turnstile/turnstile_190803.txt'
print('link_href' , link[link.find('/turnstile_')+1:])

# for i in range( 36, 40 ): #find first 4 relevant links
#     # print(soup.findAll('a')[i])
#     one_a_tag = soup.findAll('a')[i]
#     link = one_a_tag['href']        #'data/nyct/turnstile/turnstile_190803.txt', soup object?
#     download_url = 'http://web.mta.info/developers/'+ link
#     urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
#     time.sleep(1) #pause the code for a sec



# for i in range( 36,len(soup.findAll('a')) ): #'a' tags are for links
#     # print(soup.findAll('a')[i])
#     one_a_tag = soup.findAll('a')[i]
#     link = one_a_tag['href']
#     download_url = 'http://web.mta.info/developers/'+ link
#     urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
#     time.sleep(1) #pause the code for a sec
