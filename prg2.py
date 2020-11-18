
# coding: utf-8

# In[1]:


import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()#傳回值有兩個,第一個是否有讀到圖片,值為True或False,第二個是擷取當前的一禎圖片
    cv2.imshow('frame',frame)
    if cv2.waitKey(5) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

