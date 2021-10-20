#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import tree


# In[2]:


x=[[181,80,44], [177, 70, 43], [160, 60, 38], [154, 54, 37], 
   [166, 65, 40], [190, 90, 47],[175,64,39],[177,70,40], [171,75,42], [181,85,43]]


# In[3]:


y=['male','female', 'female','female', 'female', 'male', 'male', 'male', 'female', 'male']


# In[4]:


clf =tree.DecisionTreeClassifier()


# In[5]:


clf = clf.fit(x,y)


# In[6]:


predidction = clf.predict([[190,70,43]])


# In[7]:


print(predidction)


# In[ ]:




