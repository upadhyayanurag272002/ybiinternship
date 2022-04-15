#!/usr/bin/env python
# coding: utf-8

# In[124]:


import numpy as np


# In[125]:


# Creating Arrays


# In[126]:


a = np.array([1,2,3])


# In[127]:


b = np.array([(1.5,2,3), (4,5,6)], dtype = float)


# In[128]:


c = np.array([[(1.5,2,3), (4,5,6)],[(3,2,1), (4,5,6)]], dtype = float)


# In[129]:


# Initial Placeholders


# In[130]:


np.zeros((3,4)) #Create an array of zeros


# In[131]:


np.ones((2,3,4),dtype=np.int16) #Create an array of ones


# In[132]:


d = np.arange(10,25,5)#Create an array of evenly spaced values (step value)


# In[133]:


np.linspace(0,2,9) #Create an array of evenlyspaced values (number of samples)


# In[134]:


e = np.full((2,2),7)#Create a constant array


# In[135]:


f = np.eye(2) #Create a 2X2 identity matrix


# In[136]:


np.random.random((2,2)) #Create an array with random values


# In[137]:


np.empty((3,2)) #Create an empty array


# In[138]:


# I/O


# In[139]:


# Saving & Loading on Disk


# In[140]:


np.save('my_array' , a)


# In[141]:


np.savez( 'array.npz', a, b)


# In[142]:


np.load( 'my_array.npy')


# In[143]:


# Saving & Loading Text Files 


# In[119]:


np.loadtxt("myfile.txt")
np.genfromtxt("my_file.csv", delimiter= ',')
np.savetxt( "myarray.txt", a, delimiter= " ")


# In[144]:


# Asking For Help


# In[145]:


np.info(np.ndarray.dtype)


# In[146]:


# Inspecting Array 


# In[147]:


a.shape #Array dimensions


# In[148]:


len(a)#Length of array


# In[149]:


b.ndim #Number of array dimensions


# In[150]:


e.size #Number of array elements


# In[151]:


b.dtype  #Data type of array elements


# In[152]:


b.dtype.name  #Name of data type


# In[153]:


b.astype(int) #Convert an array to a different type


# In[154]:


# Data Types


# In[155]:


np.int64 #Signed 64-bit integer types


# In[156]:


np.float32 #Standard double-precision floating point


# In[157]:


np.complex128 #Complex numbers represented by 128 floats


# In[158]:


np.bool_  #Boolean type storing TRUE and FALSE values


# In[159]:


np.object_ #Python object type


# In[160]:


np.string_ #Fixed-length string type


# In[161]:


np.unicode_ #Fixed-length unicode type


# In[162]:


# Array Mathematics


# In[163]:


# Arithmetic Operations 


# In[164]:


g = a - b #Subtraction


# In[165]:


np.subtract(a,b) #Subtraction


# In[166]:


b + a #Addition 


# In[167]:


np.add(b,a) #Addition


# In[168]:


a/b #Division 


# In[169]:


np.divide(a,b) #Division


# In[170]:


a * b #Multiplication 


# In[171]:


np.multiply(a,b) #Multiplication


# In[172]:


np.exp(b) #Exponentiation


# In[173]:


np.sqrt(b) #Square root


# In[174]:


np.sin(a)  #Print sines of an array


# In[175]:


np.cos(b) #Elementwise cosine


# In[176]:


np.log(a)#Elementwise natural logarithm


# In[177]:


e.dot(f) #Dot product 


# In[178]:


# Comparison


# In[179]:


a == b #Elementwise comparison


# In[180]:


a< 2 #Elementwise comparison


# In[181]:


np.array_equal(a, b) #Arraywise comparison


# In[182]:


# Copying Arrays 


# In[183]:


h = a.view()#Create a view of the array with the same data


# In[184]:


np.copy(a) #Create a copy of the array


# In[185]:


h = a.copy() #Create a deep copy of the array


# In[186]:


# Sorting Arrays


# In[187]:


a.sort() #Sort an array


# In[188]:


c.sort(axis=0) #Sort the elements of an array's axis


# In[189]:


# Subsetting, Slicing, Indexing


# In[190]:


# Subsetting


# In[191]:


b[1,2]


# In[192]:


a[2]


# In[193]:


# Slicing


# In[194]:


a[0:2]#Select items at index 0 and 1


# In[195]:


b[0:2,1] #Select items at rows 0 and 1 in column 1


# In[196]:


b[:1] #Select all items at row0(equivalent to b[0:1, :])


# In[197]:


c[1,...] #Same as[1,:,:]


# In[198]:


a[ : : -1] #Reversed array a array([3, 2, 1])


# In[199]:


# Boolean Indexing 


# In[200]:


a[a<2] #Select elements from a less than 2


# In[201]:


# Fancy Indexing 


# In[202]:


b[[1,0,1, 0],[0,1, 2, 0]] #Select elements(1,0),(0,1),(1,2) and(0,0)


# In[203]:


b[[1,0,1, 0]][:,[0,1,2,0]] #Select a subset of the matrix’s rows and columns


# In[204]:


# Array Manipulation 


# In[205]:


# Transposing Array 


# In[206]:


i = np.transpose(b) #Permute array dimensions


# In[207]:


i.T #Permute array dimensions


# In[208]:


# Changing Array Shape 


# In[209]:


b.ravel() #Flatten the array


# In[210]:


g.reshape(3, -2) #Reshape, but don’t change data


# In[211]:


# Adding/Removing Elements


# In[212]:


h.resize((2,6)) #Return a new arraywith shape(2,6)


# In[213]:


np.append(h,g) #Append items to an array


# In[214]:


np.insert(a,1,5)  #Insert items in an array


# In[215]:


np.delete(a,[1])  #Delete items from an array


# In[216]:


# Combining Arrays 


# In[217]:


np.concatenate((a,d),axis=0) #Concatenate arrays


# In[219]:


np.vstack((a,b)) #Stack arrays vertically(row wise)


# In[220]:


np.r_[e,f] #Stack arrays vertically(row wise)


# In[221]:


np.hstack((e,f)) #Stack arrays horizontally(column wise)


# In[222]:


np.column_stack((a,d)) #Create stacked column wise arrays


# In[223]:


np.c_[a,d] #Create stacked column wise arrays


# In[224]:


# Splitting Arrays 


# In[225]:


np.hsplit(a,3) #Split the array horizontally at the 3rd index


# In[226]:


np.vsplit(c,2) #Split the array vertically at the 2nd index


# In[ ]:




