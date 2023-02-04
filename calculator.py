#!/usr/bin/env python
# coding: utf-8

# # Square numbers and return their sum

# In[1]:


class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sqSum(self):
        return self.x**2+self.y**2+self.z**2
p=Point(1,3,5)
result = p.sqSum()
print(result)


# # Implement a calculator class

# In[2]:


class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
c= Calculator(94,10)
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())


# # Implement the complete student class

# In[3]:


class Student:
    def setName(self,Name):
        self.__Name=Name
    def getName(self):
        return self.__Name
    def setRollnumber(self,Rollnumber):
        self.__Rollnumber=Rollnumber
    def getRollnumber(self):
        return self.__Rollnumber
x=Student()
x.setName("lakshmi")
x.setRollnumber("34")
print("Name:",x.getName())
print("Rollnumber:",x.getRollnumber())


# # Implement a banking account

# In[4]:


class Account:
    def __init__(self,title=0,balance=0):
        self.title=title
        self.balance=balance
class SavingsAccount(Account):
    def __init__(self,interestrate=0):
        self.interestrate=interestrate
        
x=Account("Adi",7000)
print(x.title)
print(x.balance)
y=SavingsAccount(5)
print(y.interestrate)
        


# # Handling a banking account

# In[7]:


class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance
    def withdrawl(self,amount):
        self.balance=self.balance-amount
    def deposit(self,amount):
        self.balance=self.balance+amount
    def getbalance(self):
        return self.balance    
class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestrate=0):
        super().__init__(title,balance)
        self.interestrate=interestrate
    def interestamount(self):
        return(self.balance*self.interestrate)/100        
 
x=SavingsAccount("lucky",5540,3)
print("balance",x.getbalance())
x.deposit(1000)
print("Balance after deposit:",x.getbalance())
x.withdrawl(500)
print("Balance after withdrawl:",x.getbalance())
print("interestamount:",x.interestamount())


# In[ ]:





# In[ ]:




