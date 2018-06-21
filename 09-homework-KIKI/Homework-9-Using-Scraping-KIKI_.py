
# coding: utf-8

# In[1]:


import requests

import pandas as pd
import time


# In[2]:


raw_html = requests.get ('https://www.washingtonpost.com/?reload=true').content
#print(response)


# In[3]:


from bs4 import BeautifulSoup


# In[4]:


soup_doc = BeautifulSoup(raw_html, "html.parser")
print(type(soup_doc))


# In[5]:


#print(soup_doc.prettify())
#print(soup_doc)


# In[6]:


headlines = soup_doc.find_all('div',{'class':'headline'})
summaries = soup_doc.find_all('div',{'data-pb-field':'summary'})
signatures = soup_doc.find_all('li',{'class': 'byline'})


# In[7]:


#headlines


# In[8]:


for headline in headlines:
    print('-------------')
    print(headline.text)
    try:
        #print(headline.text)
        print(headline.a['href'])
    except:
        break


# In[9]:


#for headline in headlines:
    #print('-------------')
    #print(headline.text)
    #print(headline.a['href'])


# In[10]:


for summary in summaries:
    print('----------')
    print(summary.text)


# In[11]:


for signature in signatures:
    print("--------")
    print(signature.text)


# In[12]:


homepage = []

raw_html = requests.get ('https://www.washingtonpost.com/?reload=true').content

from bs4 import BeautifulSoup

soup_doc = BeautifulSoup(raw_html, "html.parser")
#print(type(soup_doc))
#print(soup_doc)

headlines = soup_doc.find_all('div',{'class':'headline'})
summaries = soup_doc.find_all('div',{'data-pb-field':'summary'})
signatures = soup_doc.find_all('li',{'class': 'byline'})

#for info in soup_doc:
    
    #print('-------------')

dictio = {}

for headline in headlines:
        #print('-------------')
    #try:
    dictio['headline'] = headline.text

    try:
        dictio['url'] = headline.a['href']
    except:
        break

for signature in signatures:
    #print("--------")
    dictio['signature'] = signature.text

for summary in summaries:
    #print('----------')
    dictio['summary'] = summary.text 

print(dictio)
homepage.append(dictio)
#print(homepage)


# In[13]:


homepage_df=pd.DataFrame(homepage)


# In[14]:


pd.set_option('display.max_colwidth', -1)


# In[15]:


homepage_df


# In[24]:


import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%Y-%m-%d-%I%M%p")


# In[25]:


date_string


# In[44]:


file = ("briefing-"+date_string)
file


# In[50]:


homepage_df.to_csv("briefing.csv", date_format = date_string, index=False)


# In[52]:


response = requests.post(
        "https://api.mailgun.net/v3/sandbox4bfaef291e9343b1bcd73d6c2179884c.mailgun.org/messages",
        auth=("api", "XXXXXXXXXXXXXXXXXXXXXXX"),
        files=[("attachment", open(file+".csv"))],
        data={"from": "Foundations Task - Scraping <mailgun@sandbox4bfaef291e9343b1bcd73d6c2179884c.mailgun.org>",
              "to": ["kelly_kiki@yahoo.gr", "kk3289@columbia.edu"],
              "subject": ("Here is your briefing"),
              "text": "Find your today briefing attached!"}) 
response.text

