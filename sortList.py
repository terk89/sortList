#!/usr/bin/env python
# coding: utf-8

# In[4]:


a,b,c,d,e = 1, 5.5, 'c', 6.7, 'c'


# In[6]:


del a


# In[7]:


# currently stored variables
get_ipython().run_line_magic('whos', '')


# In[13]:


15%13


# # Operators
# 

# In[15]:


a = 22
type(a+b)


# In[16]:


_


# In[22]:


a = True
b = False
print (a > b)


# In[25]:


False and False or True


# In[26]:


print((not(2!=3)and True)or(False and True))


# # Useful Functions
# 

# In[31]:


round(4.54376, 2)


# In[33]:


print(divmod(2,2))


# In[43]:


print(isinstance('aksd', (float, int, bool)))
print(isinstance(3.0, float))
print(isinstance(3+3j, complex))


# In[45]:


print(pow(2,4,7))


# In[2]:


get_ipython().run_line_magic('pinfo2', 'pow')


# In[4]:


help(input)


# #Control Flow

# In[10]:


a = int(input("Podaj liczbe "))
b = int(input("Podaj druga liczbe "))
if a > b:
    print(f"Wieksza liczba to {a}")
elif a < b:
    print(f"Wieksza liczba to {b}")
else:
    print(f"Liczby {a} i {b} sa rowne")


# # LOOPS

# In[6]:


n = 10
i = 1
while True:
    if i%9 != 0:
        print("inside if")
        i += 1
        continue
    print('something')
    break
print("done")


# In[14]:


L = []
for i in range(0,10,2):
    print(i)
    L.append((i+1)**2)
    
print(L)


# In[34]:


doPosortowania = [2,1,7,66,3,-2,-2,0,-4]

for j in range(len(doPosortowania)):
    m=doPosortowania[j]
    idx = j
    counter = j
    for i in range(j,len(doPosortowania)):
        if doPosortowania[i] < m:
            m = doPosortowania[i]
            idx = counter
        counter += 1
    tmp = doPosortowania[j]
    doPosortowania[j] = m
    doPosortowania[idx] = tmp
print (doPosortowania)


# In[21]:


toRemove = [1,2,5,5,4,7,5]
toRemove.remove(5)
print(toRemove)


# In[6]:


def add(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    return sum


# In[7]:


x = add(1,2,65,4,88,2,-3)
print(x)


# In[9]:


def printAllVariableNamesAndValues(**args):
    for x in args:
        print("Variable names is:",x," And Values is:", args[x])
    


# In[10]:


printAllVariableNamesAndValues(a = 3, b='B', V = '23', j = 33)


# # Modules

# In[2]:


# package is a folder where similar modules are stored
import sys
sys.path.append('C:/Users/matte/OneDrive/Dokumenty/Python Scripts/')


# In[7]:


from my_universal_functions import addAllNumerics as aan


# In[9]:


get_ipython().run_line_magic('pinfo2', 'aan')


# In[8]:


aan(1,2,3,4)


# # Practice Functions 07:03:00

# In[54]:


#sorting the list
from my_universal_functions import checkIfNotNumeric

def findMin(L):
    m = L[0]
    idx = 0
    counter = 0 
    for x in L:
        if x < m:
            m = x
            idx = counter
        counter += 1
    return m, idx

#swaping the values
def swapValues(L, idx1, idx2):
    tmp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = tmp
    return L
    
def sortList(L):
    for i in L:
        if not(checkIfNotNumeric(i)):
            print("Error: List does not contain numeric values")    
        else:
            counter = 0
            for x in L:
                m,idx = findMin(L[counter:])
                L = swapValues(L,(idx+counter),counter)            
                counter +=1
            return L
     


# In[16]:


a,b = findMin([1,2,3,4,5,-3])
print(f'The minimum value is {a}, located at the index {b}.')


# In[18]:


swapValues([1,2,3,4], 2, 3)


# In[56]:


L2 = [-1,2,-4,2,6,3,0,-4]
print(sortList(L2))


# In[53]:


print(findMin(L2[2:]))


# In[ ]:




