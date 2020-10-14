#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
html_doc="""<html><head><title>Hello World</title></head>
<body><h2>洪臺聲</h2>
<p>ADT107125</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>"""
soup=BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())


# In[2]:


title_tag=soup.title
print(title_tag)


# In[3]:


a_tags=soup.find_all('a')
for tag in a_tags:
    print(tag)
    print(tag.string)


# In[4]:


for tag in a_tags:
    print(tag.get('href'))


# In[5]:


for tag in a_tags:
    print('連結:'+tag.string+'=>'+tag.get('href'))


# In[ ]:




