#!/usr/bin/env python
# coding: utf-8

# In[1]:


def digit_count(n):
    zero=0
    even=0
    odd=0
    while (n>0):
        rem=n%10 #remainder
        if(rem==0):
            zero+=1
        if(rem %2==0 and rem!=0):
            even+=1
        if(rem%2 !=0 and rem!=0):
            odd+=1
        n=int(n/10)
        
    c=(even,odd,zero)
    return c

a=float(input())
digit_count(a)


# In[ ]:




