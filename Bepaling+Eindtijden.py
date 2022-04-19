
# coding: utf-8

# # General
# Template for labjournaal. See https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html for options to use markdown.
# 
# **Name:**  
# **Title of the experiment:**  
# **Starting date:**  
# **Expected enddate:**  
# **Partner:**  
# **Goal of the experiment:**  
# **Research question:**  
# **Expectations or Hypothesis:**  
# **Desired accuracy:**  
# 
# 
# 

# In[1]:


#import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit 
import csv
import traceback
import sys
from tools import Ruler

get_ipython().magic('matplotlib notebook')


# In[ ]:





# # Preparation
#  
# 

# **Assignments:**  

# **Method:**  
# **Theory:**  
# **Independent variable:**  
# **Dependent variable:**  
# **Controlled variablen:**  
# **Measurement instruments \& Settings:**  
# **Procedure:**  
# **Setup(drawing or picture):**  
# **Notes:**  
# **About accuracy:**  
# 

# # Execution

# In[2]:


# Measurements: Explain the names of variables provide only raw data in np.arrays!

def aflezen(n):
    n = str(n)
    rows = []
    f = open("Amplitudes"+n+".csv", 'r')
    csvreader = csv.reader(f)
    header = next(csvreader)
    
    for row in csvreader:
            rows.append(row)
    
    print(header)
    
    f.close()
    
    
    x = []
    y = []
    
    i = -1
    for el in rows:
        i += 1
        if el[1] != '-∞':
            x.append(float(el[0]))
            y.append(float(el[1]))
        else:
            print('inf at positon:', i)
    
    return x, y

def linverg(x, a, b):
    return a*x+b

def verwijder(x, y, lower, upper):
    f = np.array([])
    g = np.array([])
    
    i = -1
    for elt in x:
        i += 1
        if elt >= lower and elt <= upper:
            f = np.append(f, elt)
            g = np.append(g, y[i])
    
    g = g - g[0]
    
    waardes, covariantie = curve_fit(linverg, f, g)
    a, b = waardes
    print(waardes)

    t = np.linspace(lower, upper, 1000)
    
    plt.figure()
    plt.plot(f, g, 'r.')
    plt.plot(t, a*t+b)
    plt.grid(which = 'both')
    plt.xticks(np.arange(lower, upper, 1))
    plt.yticks(np.arange(g[-1], g[0], 5))
    plt.hlines(20*np.log10(0.04), lower, upper, 'g')
    plt.show()
    
    print(f[0])
    print(np.sqrt(np.diag(covariantie)))


# **Observations:**  
# **Notes:**  

# # Processing
# **Description of processing of raw data into scientific evidence:**
# 

# In[3]:


x, y = aflezen(1)
verwijder(x, y, 9.3, 16.46)


# In[4]:


x, y = aflezen(2)
verwijder(x, y, 8.16, 14.92)


# In[5]:


x, y = aflezen(3)
verwijder(x, y, 7.88, 16.12)


# In[6]:


x, y = aflezen(4)
verwijder(x, y, 8.76, 18.11)


# In[7]:


x, y = aflezen(5)
verwijder(x, y, 8.75, 18.75)


# In[8]:


x, y = aflezen(6)
verwijder(x, y, 7.71, 18.31)


# In[9]:


x, y = aflezen(7)
verwijder(x, y, 10.95, 19.52)


# In[10]:


x, y = aflezen(8)
verwijder(x, y, 16.51, 23.95)


# In[11]:


x, y = aflezen(9)
verwijder(x, y, 5.74, 12.31)


# In[12]:


x, y = aflezen(10)
verwijder(x, y, 15.29, 21.13)


# In[13]:


x, y = aflezen(11)
verwijder(x, y, 5.11, 8.32)


# In[14]:


x, y = aflezen(12)
verwijder(x, y, 3.53, 8.10)


# In[15]:


a = np.array([-5.81019165, -6.86292675, -5.43162245, -5.03493479, -5.09453856, -4.3665042, -5.28298813, -6.26683545, -8.17621133, -8.6845426, -15.094226, -9.14726099])


# **Describing the pattern in the processed data:**  
# 

# In[16]:


#Calculations of e.a. measurement uncertainties, and providing final answers.
u_a = np.array([0.27047015, 0.18164875, 0.13959377, 0.18262388, 0.13214084, 0.06981853, 0.11808407, 0.34469029, 0.20888799, 0.71357976, 0.88157823, 0.57128945])


# **Notes:**  

# # Discussion
# 
# 

# # Conclusion

# In[ ]:





# In[ ]:





# # Additional notes, remarks, explanations, thoughts etc

# 
