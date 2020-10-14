#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import bs4
url='https://dct.ntcu.edu.tw/news.php'
html=requests.get(url)
html.encoding='utf-8'
print(html.text)


# In[2]:


htmllist=html.text.splitlines()
for row in htmllist:
    print(row)


# In[3]:


n=0
keyword="數位"
for row in htmllist:
    if keyword in row:n+=1
        
print("找到{}!".format(n))

