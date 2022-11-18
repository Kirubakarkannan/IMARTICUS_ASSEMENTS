#!/usr/bin/env python
# coding: utf-8

# In[94]:


def itfruit():
    fruits=["Apple","Banana","Apricot","Atemoya","Avocados","Blueberry","Blackcurrant","Ackee","Cranberry","Cantaloupe","Cherry","Black sapote","Chocolate pudding fruit","Dragonrfruit","Dates","Cherimoya","Buddha’s hand fruit","Finger Lime","Fig","Coconut","Cape gooseberry","Inca berry","Physalis","Grapefruit","Gooseberries","Custard apple","Sugar apple","Sweetsop","Chempedak","Hazelnut","Honeyberries","Dragon fruit","Durian","Horned Melon","Hog Plum","Egg fruit","Feijoa","Pineapple guava","Guavasteen","Indian Fig","Ice Apple","Guava","Fuyu Persimmon","Jackfruit","Jujube","Honeydew melon","Jenipapo","Kiwi","Kabosu","Kiwano","Kaffir lime","Makrut Lime","Lime","Lychee","Longan","Langsat","Mango","Mulberry","Pear","Lucuma","Muskmelon","Naranjilla","Passion fruit","Mangosteen","Nectarine","Nance","Quince","Medlar fruit","Olive","Oranges","Ramphal","Mouse melon","Papaya","Peach","Rose apple","Water apple","Noni fruit","Pomegranate","Pineapple","Rambutan","Snake fruit","Salak","Raspberries","Strawberries","Starfruit","Carambola","Soursop","Tangerine","Olive","Oranges","Ramphal","Mouse melon","Papaya","Peach","Rose apple","Water apple","Noni fruit","Watermelon","Sapota","Star apple"]
    fruits.sort()
    n=int(len(fruits)-1)
    for n in fruits:
            print(n)
   
    


# In[95]:


def menu():
    num=int(input("Enter the number"))
    if(num%2==0):
        print("The number",num," is even")
    else:
        print("The number",num,"is odd")
    itfruit()


# In[96]:


def login():
    Un=input("enter user name")
    Pd=input("enter the password")
    for u in Users:
        if Un==u[0]:
            if Pd==u[1]:
                print("Login sucessful")
                menu()
            else:
                print("Invalid credentials")
            


# In[97]:


Users=[['User1','Pass1'],['User2','Pass2'],['User3','Pass3'],['User4','Pass4']]


# In[98]:


username = login()


# In[ ]:




