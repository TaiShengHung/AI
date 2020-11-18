
# coding: utf-8

# In[1]:


import cv2
cap = cv2.VideoCapture(0)       
while(True):
    ret, frame = cap.read()
    cv2.imshow("frame", frame)     
    if cv2.waitKey(1) == ord('q'):   
        cv2.imwrite("test.png", frame) #儲存路徑
        break

cap.release()
cv2.destroyAllWindows()

