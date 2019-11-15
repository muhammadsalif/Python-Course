
# coding: utf-8

# In[9]:


s = int(input("Enter Subject1 marks!"))
j = int(input("Enter Subject2 marks!"))
k = int(input("Enter Subject3 marks!"))
l = int(input("Enter Subject4 marks!"))
m = int(input("Enter Subject5 marks!"))
ObtainMarks = s+j+k+l+m
Percentage= (ObtainMarks/500) * 100
if(Percentage >= 80 and Percentage <= 100):
    print("Grade is A+")
elif(Percentage >= 70 and Percentage< 80):
    print("Grade is A")
elif(Percentage >= 60 and Percentage < 70):
    print("Grade is B")
elif(Percentage >= 50 and Percentage < 60):
    print("Grade is C")
elif(Percentage >= 0 and Percentage < 50): 
    print("fail!")
else:
    print("You put wrong num:")


# In[17]:


num = int(input("ENter a Num !"))
if(num % 2 == 0 ):
    print("Num is even:")
else:
    print("Num is odd:")
    


# In[26]:


list1 = [1,2,3,4,5,6]
count = 0
for x in range(len(list1)):
     count += 1
print(count)


# In[28]:


list1 = [1,2,3,4,5,6]
sum = 0
for x in range(len(list1)):
     sum = list1[x] + sum 
print(sum)


# In[36]:


import sys
list1 = [-1,-2,-3,-4,-5,-34]
max1 = -sys.maxsize -1
for x in range(len(list1)):
    if(list1[x] > max1 ):
      max1 = list1[x]
print(max1)


# In[38]:


list1 = [0,1,2,3,4,5,6]
for x in range(len(list1)):
     if(list1[x] < 5):
             print(list1[x])

