
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



# **Observations:**  
# **Notes:**  

# # Processing
# **Description of processing of raw data into scientific evidence:**
# 

# In[ ]:





# In[3]:


#dingen die we direct meten
lengtes = np.array([0.645, 0.6075, 0.574])
f = np.array([251.09, 264.65, 280.05, 296.66, 317.89, 330.74, 352.11, 396.36, 419.93, 442.88, 444.52, 474.28])


Tb = np.array([9.31, 8.31, 7.91, 8.92, 8.76, 7.72, 11.14, 16.52, 5.91, 15.32, 5.12, 3.72])
Te = np.array([12.492, 11.92, 12.60, 13.50, 13.22, 13.61, 15.90, 19.80, 8.8, 17.02, 6.79, 6.20])


# In[22]:


#onzekerheden

u_Tb = 0.2
u_Te = 0.5

u_T = np.sqrt(u_Tb**2+u_Te**2)
print(u_T)
u_Q = f * u_T
print(u_Q)


# **Describing the pattern in the processed data:**  
# 

# In[5]:


#Calculations of e.a. measurement uncertainties, and providing final answers.
Ttot = Te - Tb
print(Ttot)
Q = Ttot * f
print(Q)


# In[6]:


a = np.array([-5.81019165, -6.86292675, -5.43162245, -5.03493479, -5.09453856, -4.3665042, -5.28298813, -6.26683545, -8.17621133, -8.6845426, -15.094226,  -9.14726099])
delta = - np.log(10) * a / 20

Qmvs = np.sqrt(4*(np.pi**2)*(f**2)+delta**2)/(2*delta)
print(Qmvs)
print(Q/Qmvs)


# In[25]:


u_a = np.array([0.27047015, 0.18164875, 0.13959377, 0.18262388, 0.13214084, 0.06981853, 0.11808407, 0.34469029, 0.20888799, 0.71357976, 0.88157823, 0.57128945])
u_delta = np.log(10) * u_a / 20



u_Qmvs = abs(4*np.pi**2*f**2*u_delta/(delta**2*np.sqrt(4*(np.pi**2)*(f**2)+delta**2)))

print(u_Qmvs/u_delta)
print(4*np.pi**2*f/(2*deltanp.sqrt(4*(np.pi**2)*(f**2)+delta**2)))

for i in range(12):
    if abs(Q[i]-Qmvs[i]) > 2*np.sqrt((u_Qmvs[i])**2+(u_Q[i])**2):
        print('voor meting ', i, ': strijdig')
    else:
        print('voor meting ', i, ': niet strijdig')


# In[20]:


get_ipython().magic('matplotlib notebook')
plt.figure()
plt.errorbar(f, Q, yerr=u_Q, label='Definitie', fmt='.')
plt.errorbar(f, Qmvs, yerr=u_Qmvs, label='Massa-veer benadering', fmt='.')
plt.xlabel('Frequentie (Hz)')
plt.ylabel('Q-factor')
plt.legend()
plt.savefig('Q-factor.png')
plt.show()


# **Notes:**  

# # Discussion
# 
# 

# # Conclusion

# In[ ]:





# In[ ]:





# # Additional notes, remarks, explanations, thoughts etc

# 
