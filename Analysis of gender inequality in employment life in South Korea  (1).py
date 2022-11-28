#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib


# In[3]:


raw_welfare = pd.read_spss('Koweps_hpc16_2021_beta1.sav')
welfare = raw_welfare.copy()


# In[4]:


welfare = welfare.rename(
    columns = {'h16_g3' : 'sex',
               'p1602_8aq1' : 'income',
              'h16_g4' : 'birth'})
               


# In[4]:


welfare['sex'].dtypes


# In[ ]:


welfare['sex'].value_counts()


# In[27]:


welfare['sex'] = np.where(welfare['sex'] == 1, 'male', 'female')
welfare['sex'].value_counts()


# In[ ]:


sns.countplot(data = welfare, x= 'sex')


# In[15]:


welfare['income'].dtypes


# In[18]:


welfare['income'].describe() #‘Monthly wage’ means the average monthly wage for one month and is recorded in units of 10,000 won. (converted euro to 7.16 euro)


# In[19]:


sns.histplot(data = welfare, x= 'income')


# In[20]:


welfare['income'].isna().sum()


# In[40]:


sex_income = welfare.dropna(subset = ['income'])                     .groupby('sex', as_index = False)                    .agg(mean_income = ('income', 'mean'))

sex_income


# In[42]:


sns.barplot(data = sex_income, x = 'sex', y = 'mean_income')


# In[6]:


welfare['birth'].describe()


# In[8]:


sns.histplot(data = welfare, x = "birth")


# In[9]:


welfare = welfare.assign(age = 2020 - welfare['birth'] + 1)
welfare['age'].describe()


# In[10]:


sns.histplot(data = welfare, x = 'age')


# In[11]:


age_income = welfare.dropna(subset = ['income'])                     .groupby('age')                     .agg(mean_income = ('income', 'mean'))
age_income.head()


# In[12]:


sns.lineplot(data = age_income, x = 'age', y = 'mean_income')


# In[13]:


welfare['age'].head()


# In[14]:


welfare = welfare.assign(ageg = np.where(welfare['age'] < 30, 'young', np.where(welfare['age'] <= 59, 'middle', 'old')))

welfare['ageg'].value_counts()


# In[15]:


sns.countplot(data = welfare, x = 'ageg')


# In[24]:


sns.barplot(data = ageg_income, x = 'ageg', y = 'mean_income', order = ['young', 'middle', 'old'])


# In[28]:


sex_income =     welfare.dropna(subset = ['income'])             .groupby(['ageg', 'sex'], as_index = False)             .agg(mean_income = ('income', 'mean'))

sex_income


# In[29]:


sns.barplot(data = sex_income, x = 'ageg', y = 'mean_income', hue = 'sex', order = ['young', 'middle', 'old'])


# In[31]:


sns.lineplot(data = sex_age, x = 'age', y = 'mean_income', hue = 'sex')


# In[ ]:





# In[ ]:




