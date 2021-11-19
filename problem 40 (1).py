#!/usr/bin/env python
# coding: utf-8

# In[ ]:


height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
height =height/100
BMI = weight / (height)**2
print ("BMI = ")
print (BMI)


# In[ ]:


height = float(input("Enter your height in inch: "))
weight = float(input("Enter your weight in pound: "))
height = height/39.37
weight = weight/2.2
BMI = weight / (height)**2
print ("BMI = ")
print (BMI)

