#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, shutil


# In[13]:


path = r"C:/Users/SiMaker/Desktop/Python Practice/"


# In[14]:


fileos.listdir(path)


# In[22]:


folder_names = ['csv files', 'image files', 'audio files', 'software files', 'pdf files']

for loop in range(0,5):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])
        
for file in file_name:
    if ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".xlsx" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif ".mp4" in file and not os.path.exists(path + "audio files/" + file):
        shutil.move(path + file, path + "audio files/" + file)
    elif ".exe" in file and not os.path.exists(path + "software files/" + file):
        shutil.move(path + file, path + "software files/" + file)


# In[17]:


file_name = os.listdir(path)


# In[26]:


for file in file_name:
    if ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".xlsx" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif ".mp4" in file and not os.path.exists(path + "audio files/" + file):
        shutil.move(path + file, path + "audio files/" + file)
    elif ".exe" in file and not os.path.exists(path + "software files/" + file):
        shutil.move(path + file, path + "software files/" + file)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




