#!/usr/bin/env python
# coding: utf-8

# In[8]:


from __future__ import print_function, unicode_literals 
import json
from facepplib import FacePP, exceptions 
import emoji 
# define global variables 
face_detection = "" 
faceset_initialize = "" 
face_search = "" 
face_landmarks = "" 
dense_facial_landmarks = "" 
face_attributes = "" 
beauty_score_and_emotion_recognition = "" 
   
# define face comparing function 
def face_comparing(app): 

    print('Comparing Photographs......')   
    image1 = 'https://cdn.britannica.com/25/162425-050-B767198B/Aamir-Khan.jpg'
    image2 = 'https://c.ndtvimg.com/2023-09/e6ijd1u_priyanka-_625x300_04_September_23.jpg'
    cmp_ = app.compare.get(image_url1 = image1, image_url2 = image2) 
   
    print('Photo1', '=', cmp_.image1) 
    print('Photo2', '=', cmp_.image2) 
   
    # Comparing Photos 
    if cmp_.confidence > 50 :
        #print(cmp_.confidence)
        print('Same Persons Image')
    else: 
        #print(cmp_.confidence)
        print('2 Difference Persons Image') 
  

        
# Driver Code  
if __name__ == '__main__': 
   
    # api details 
    api_key ='xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
    api_secret ='TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'
    
    try:
        
        app_ = FacePP(api_key = api_key,  api_secret = api_secret) 
        funcs = [ 
            face_detection, 
            faceset_initialize, 
            face_search, 
            face_landmarks, 
            dense_facial_landmarks, 
            face_attributes, 
            beauty_score_and_emotion_recognition 
        ] 
        face_comparing(app_) 
           
    except exceptions.BaseFacePPError as e: 
        print('Error:', e) 
  


# In[ ]:




