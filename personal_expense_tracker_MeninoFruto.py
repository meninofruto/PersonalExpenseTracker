#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import os
from utility import *
expense_list = []
budget = 0
exit_code = 0


# In[2]:


load_expense_csv()


# In[3]:


while True:
    exit_code = menu()
    if exit_code==5:
        break



# In[ ]:




