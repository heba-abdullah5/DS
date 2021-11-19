#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def count(x):
    v=0 #the total number of vowels
    c=0 #the total number of consonants
    a1=a.lower()
    for i in a1:
        if (i=='a' or i=='o' or i=='i' or i=='e'or i=='u'):
            v+=1
        else:
            c+=1
    print("the total number of vowels",v)
    print("the total number of consonants",c)
a=str(input("inter an english sentenc: "))
count(a)


# In[ ]:





# In[ ]:




