#!/usr/bin/env python
# coding: utf-8

# In[87]:


import pandas as pd
import numpy as np
import scipy.stats as stats 
import matplotlib.pyplot as plt
import sklearn

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import GridSearchCV,train_test_split 
from sklearn.metrics import mean_absolute_error

data=pd.read_csv("C:\\Users\\Ram\\Desktop\\graduate-admissions-predictor\\Admission_Predict.csv");
data
admissions = data.drop('Serial No.',axis = 1)
admissions


# In[100]:


x = admissions.drop('Chance_of_Admit',axis = 1)
y = admissions['Chance_of_Admit']

X_train,X_val,y_train,y_val = train_test_split(x,y,test_size = .30,random_state = 123)


# In[101]:


x


# In[102]:


X_val


# In[103]:


y_val


# In[104]:


rf_model = RandomForestRegressor()
rf_model.fit(X_train,y_train)
print('Mean absolute error for RF model: %0.4f' %mean_absolute_error(y_val,rf_model.predict(X_val)))


# In[105]:


new_ip = [[330,113,5,5.0,4.0,9.31,1]]
rf_model.predict(new_ip)


# In[107]:



new_ip = [[336,119,5,4,3.5,9.8,1]]
rf_model.predict(new_ip)


# In[109]:


import pickle
pickle.dump(rf_model, open('model.pkl','wb'),protocol=2)


# In[ ]:




