#!/usr/bin/env python
# coding: utf-8

# In[1]:


# print 0 to 20 by using range


# In[2]:


for num in range(0,20):
    print(num)


# In[3]:


# print range 10 to 20


# In[4]:


for num in range(10, 20):
    print(num, end=" ")


# In[5]:


# Print number of items in the list by using 'len'


# In[6]:


print("[10, 20, 14, 55, 43, 87, 76]")
print("The number item in the List2:")
print(len([10, 20, 14, 55, 43, 87, 76])) 


# In[7]:


text = "Artificial Intelligence"
print(text)
for L in text:
    print(L)


# In[8]:


lists = ["-Your Name-", "-Your Age-", "-Your Profession-"]

for L in lists:
    print(L)


# In[9]:


# Refer this link : https://www.geeksforgeeks.org/python-tuples/
# Print yhis mixered datatype using Tuples


# In[10]:


tup = (1,'Welcome',2, 'Hope')
print(tup)


# In[11]:


# Refer this link : https://www.geeksforgeeks.org/python-tuples/
Tuple1 = (0, 1, 2, 3)


# In[12]:


tup1 = ((0, 1, 2, 3))
tup2 = (('python', 'HOPE'))
tup3 = tup1 + tup2
print(tup3)


# In[13]:


# print Odd Numbers in the list


# In[47]:


L=(20, 10, 16, 19, 25, 1, 276, 188)
print(L)
for n in L:
    if ((n%2)!=0):
        print(n,"is Odd")


# In[45]:


# print Even numbers in the list


# In[46]:


L=(20, 10, 16, 19, 25, 1, 276, 188)
print(L)
for n in L:
    if ((n%2)==0):
        print(n,"is Even")


# In[ ]:




