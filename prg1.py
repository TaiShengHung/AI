
# coding: utf-8

# In[1]:


import cv2 #引入opencv函式庫
cv2.__version__ 


# In[2]:


img = cv2.imread('start1.png')
cv2.imshow('My Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

