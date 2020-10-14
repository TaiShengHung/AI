#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import bs4
url='https://dct.ntcu.edu.tw/news.php'
html=requests.get(url)
html.encoding='utf-8'
print(html.text)


# In[ ]:




