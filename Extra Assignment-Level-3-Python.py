#!/usr/bin/env python
# coding: utf-8

# In[1]:


# print 'CORRECT' if i == 10


# In[8]:


num=int(input("Value:"))
if(num==10):
    print("Correct")

    


# In[9]:


# Check the password, using if and else


# In[14]:


pwd=input("Enter the password:")
if(pwd=="HOPE@123"):
    print("Your password is correct")


# In[15]:


# Catagory the people by their age like children, adult, citizen, senior citizen...


# In[22]:


age=int(input("Age: "))
if(age<18):
        print("Children")
elif(age<35):
    print("Adult")
elif(age<59):
    print("Citizen")
else:
    print("Senior Citizen")


# In[23]:


# Find whether given number is positive or negative


# In[25]:


num=int(input("Enter any number:"))
if((num%2)!=0):
    print("No is Positive")


# In[26]:


# Check whether the given number is divisible by 5


# In[27]:


num=int(input("Enter a number to check:"))
if((num%5)==0):
    print("No is divisible by 5")
else:print("No is not divisible by 5")


# In[ ]:




