#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random
import string

print('Random Password generator!')

len = int(input('\nEnter the length of password: '))

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
number = string.digits
symbols = string.punctuation

char = lowercase + uppercase + number + symbols

temp = random.sample(char,len)
password = "".join(temp)

print(password)

