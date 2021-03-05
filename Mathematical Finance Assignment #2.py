#!/usr/bin/env python
# coding: utf-8

# In[88]:


import matplotlib.pyplot as plt


# In[89]:


GP=[]

    
for i in range(52):
    powers=[]
    for j in range(i+1):
        powers.append(1.1**(-i+2*j))
    GP.append(powers)

print(GP)
        


# In[90]:


ACP=[]
for j in range(len(GP)):
    ACP.append([])

for j in range(len(GP)):
    for i in range (len(GP[51-j])):
        if j==0:
            ACP[51-j].append(max(0,GP[51][i]-1))
        else:
            ACP[51-j].append(max(0,(11/21)*ACP[51-j+1][i]+(10/21)*ACP[51-j+1][i+1],GP[51-j][i]-1))
print(ACP)


# In[91]:


UP2=[]
for j in range(len(GP)):
    UP2.append([])
    
for j in range(len(GP)):
    for i in range (len(GP[51-j])):
        if j==0:
            UP2[51-j].append(max(0,ACP[51][i]))
        elif j==1:
            UP2[51-j].append(max(0,(11/21)*UP2[51-j+1][i]+(10/21)*UP2[51-j+1][i+1]+max(0,GP[51-j][i]-1)))
        else:
            UP2[51-j].append(max(0,(11/21)*UP2[51-j+1][i]+(10/21)*UP2[51-j+1][i+1],(11/21)*ACP[51+1-j][i]+(10/21)*ACP[51+1-j][i+1]+max(0,GP[51-j][i]-1)))
print(UP2)


# In[92]:


UP3=[]
for j in range(len(GP)):
    UP3.append([])
    
for j in range(len(GP)):
    for i in range (len(GP[51-j])):
        if j==0:
            UP3[51-j].append(max(0,ACP[51-j][i]))
        elif j==1:
            UP3[51-j].append(max(0,(11/21)*UP3[51-j+1][i]+(10/21)*UP3[51-j+1][i+1]+max(0,GP[51-j][i]-1)))
        elif j==2:
            UP3[51-j].append(max(0,(11/21)*UP3[51-j+1][i]+(10/21)*UP3[51-j+1][i+1]+max(0,GP[51-j][i]-1)))
        else:
            UP3[51-j].append(max(0,(11/21)*UP3[51-j+1][i]+(10/21)*UP3[51-j+1][i+1],(11/21)*UP2[51+1-j][i]+(10/21)*UP2[51+1-j][i+1]+max(0,GP[51-j][i]-1)))
print(UP3)


# In[94]:


UP4=[]
for j in range(len(GP)):
    UP4.append([])
    
for j in range(len(GP)):
    for i in range (len(GP[51-j])):
        if j==0:
            UP4[51-j].append(max(0,ACP[51-j][i]))
        elif j==1:
            UP4[51-j].append(max(0,(11/21)*UP4[51-j+1][i]+(10/21)*UP4[51-j+1][i+1]+max(0,GP[51-j][i]-1)))
        elif j==2:
            UP4[51-j].append(max(0,(11/21)*UP4[51-j+1][i]+(10/21)*UP4[51-j+1][i+1]+max(0,GP[51-j][i]-1)))
        elif j==3:
            UP4[51-j].append(max(0,(11/21)*UP4[51-j+1][i]+(10/21)*UP4[51-j+1][i+1]+max(0,GP[51-j][i]-1)))
        else:
            UP4[51-j].append(max(0,(11/21)*UP4[51-j+1][i]+(10/21)*UP4[51-j+1][i+1],(11/21)*UP3[51+1-j][i]+(10/21)*UP3[51+1-j][i+1]+max(0,GP[51-j][i]-1)))
print(UP4)


# In[95]:


ON=[]
NON=[]

for i in range(len(UP4)):
    for j in range(len(UP4[i])):
        if i==51:
            if UP4[i][j]>0:
                ON.append([i,j])
            else:
                NON.append([i,j])
        elif i==50:
            if UP4[i][j]>0:
                ON.append([i,j])
            else:
                NON.append([i,j])
        elif i==49:
            if UP4[i][j]>0:
                ON.append([i,j])
            else:
                NON.append([i,j])
        elif i==48:
            if UP4[i][j]>0:
                ON.append([i,j])
            else:
                NON.append([i,j])
        else:
            if UP4[i][j]==UP3[i][j]+max(0,GP[i][j]-1):
                ON.append([i,j])
            else:
                NON.append([i,j])


yes=[[ON[i][0], 1.1**(-ON[i][0]+2*ON[i][1])] for i in range(len(ON))]
no=[[NON[i][0], 1.1**(-NON[i][0]+2*NON[i][1])] for i in range(len(NON))]



yesx= [yes[i][1] for i in range(len(yes))]
yesy= [yes[i][0] for i in range(len(yes))]

nox=[no[i][1] for i in range(len(no))]
noy=[no[i][0] for i in range(len(no))]


plt.rcParams['figure.figsize'] = [20, 10]

plt.plot(yesx,yesy,'b.', label='Optimal exercise')
plt.plot(nox,noy,'r.')

plt.title("Optimal Exercise Nodes for the 4-Up-Swing Option")
plt.xlabel("Gasonline Price $/L")
plt.ylabel("Week")

plt.legend()
plt.show()


# In[50]:


APP=[]
for j in range(len(GP)):
    APP.append([])

for j in range(len(GP)):
    for i in range (len(GP[51-j])):
        if j==0:
            APP[51-j].append(max(0,1-GP[51][i]))
        else:
            APP[51-j].append(max(0,(11/21)*APP[51-j+1][i]+(10/21)*APP[51-j+1][i+1],1-GP[51-j][i]))
print(APP)


# In[96]:


D2=[]
for j in range(len(GP)):
    D2.append([])
    
for j in range(len(GP)):
    for i in range (len(GP[51-j])):
        if j==0:
            D2[51-j].append(max(0,APP[51][i]))
        elif j==1:
            D2[51-j].append(max(0,(11/21)*D2[51-j+1][i]+(10/21)*D2[51-j+1][i+1]+max(0,1-GP[51-j][i])))
        else:
            D2[51-j].append(max(0,(11/21)*D2[51-j+1][i]+(10/21)*D2[51-j+1][i+1],(11/21)*APP[51+1-j][i]+(10/21)*APP[51+1-j][i+1]+max(0,1-GP[51-j][i])))
print(D2)


# In[97]:


D3=[]
for j in range(len(GP)):
    D3.append([])
    
for j in range(len(GP)):
    for i in range (len(GP[51-j])):
        if j==0:
            D3[51-j].append(max(0,APP[51-j][i]))
        elif j==1:
            D3[51-j].append(max(0,(11/21)*D3[51-j+1][i]+(10/21)*D3[51-j+1][i+1]+max(0,1-GP[51-j][i])))
        elif j==2:
            D3[51-j].append(max(0,(11/21)*D3[51-j+1][i]+(10/21)*D3[51-j+1][i+1]+max(0,1-GP[51-j][i])))
        else:
            D3[51-j].append(max(0,(11/21)*D3[51-j+1][i]+(10/21)*D3[51-j+1][i+1],(11/21)*D2[51+1-j][i]+(10/21)*D2[51+1-j][i+1]+max(0,1-GP[51-j][i])))
print(D3)


# In[98]:


D4=[]
for j in range(len(GP)):
    D4.append([])
    
for j in range(len(GP)):
    for i in range (len(GP[51-j])):
        if j==0:
            D4[51-j].append(max(0,APP[51-j][i]))
        elif j==1:
            D4[51-j].append(max(0,(11/21)*D4[51-j+1][i]+(10/21)*D4[51-j+1][i+1]+max(0,1-GP[51-j][i])))
        elif j==2:
            D4[51-j].append(max(0,(11/21)*D4[51-j+1][i]+(10/21)*D4[51-j+1][i+1]+max(0,1-GP[51-j][i])))
        elif j==3:
            D4[51-j].append(max(0,(11/21)*D4[51-j+1][i]+(10/21)*D4[51-j+1][i+1]+max(0,1-GP[51-j][i])))
        else:
            D4[51-j].append(max(0,(11/21)*D4[51-j+1][i]+(10/21)*D4[51-j+1][i+1],(11/21)*D3[51+1-j][i]+(10/21)*D3[51+1-j][i+1]+max(0,1-GP[51-j][i])))
print(UP4)


# In[101]:


ON=[]
NON=[]

for i in range(len(D4)):
    for j in range(len(D4[i])):
        if i==51:
            if D4[i][j]>0:
                ON.append([i,j])
            else:
                NON.append([i,j])
        elif i==50:
            if D4[i][j]>0:
                ON.append([i,j])
            else:
                NON.append([i,j])
        elif i==49:
            if D4[i][j]>0:
                ON.append([i,j])
            else:
                NON.append([i,j])
        elif i==48:
            if D4[i][j]>0:
                ON.append([i,j])
            else:
                NON.append([i,j])
        else:
            if D4[i][j]==D3[i][j]+max(0,1-GP[i][j]):
                ON.append([i,j])
            else:
                NON.append([i,j])


yes=[[ON[i][0], 1.1**(-ON[i][0]+2*ON[i][1])] for i in range(len(ON))]
no=[[NON[i][0], 1.1**(-NON[i][0]+2*NON[i][1])] for i in range(len(NON))]



yesx= [yes[i][1] for i in range(len(yes))]
yesy= [yes[i][0] for i in range(len(yes))]

nox=[no[i][1] for i in range(len(no))]
noy=[no[i][0] for i in range(len(no))]


plt.rcParams['figure.figsize'] = [20, 10]

plt.plot(yesx,yesy,'b.', label='Optimal exercise')
plt.plot(nox,noy,'r.')

plt.title("Optimal Exercise Nodes for the 4-Down-Swing Option")
plt.xlabel("Gasonline Price $/L")
plt.ylabel("Week")

plt.legend()
plt.show()


# In[ ]:





# In[20]:





# In[ ]:





# In[ ]:





# In[3]:





# In[ ]:




