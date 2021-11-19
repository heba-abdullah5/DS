#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def password():
    while True:
        password = input("Enter a password: ")
        if len(password) > 5 and len(password) <21:
            password.isupper() and password.islower()and password.isdigit()
            print("the password is valid")
            
        else:
            print("the password is not valid.")
            break

password()


# In[ ]:




