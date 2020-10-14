#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
url = 'https://dct.ntcu.edu.tw/news_content.php'
r = requests.get(url)

if r.status_code == requests.codes.ok:
  
  soup = BeautifulSoup(r.text, 'html.parser')

  a_tags = soup.find_all('a')
  for tag in a_tags:
    #print(tag.string)
    #print(tag.get('href'))   
    
    print('網址：'+str(tag.string)+' -> '+tag.get('href'))    
   

