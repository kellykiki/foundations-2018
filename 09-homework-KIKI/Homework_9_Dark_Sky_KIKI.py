
# coding: utf-8

# In[1]:


import requests


# In[2]:


response = requests.get ('https://api.darksky.net/forecast/e6eaf0acc80ba398537016a06622c4e6/40.7127753,-74.0059728')
print(response)


# In[3]:


newyork=response.json()

Right now it is TEMPERATURE degrees out and SUMMARY. 
Today will be TEMP_FEELING with a high of HIGH_TEMP and a low of LOW_TEMP. RAIN_WARNING.
# In[4]:


if newyork['currently']['icon'] == 'rain':
    body = "Right now it is {} degrees out and it is {}. Today will be {} with a high of {} and a low of {}. Rain warning: Bring your umbrella!".format(newyork['currently']['temperature'], newyork['currently']['summary'], newyork['currently']['apparentTemperature'], newyork['daily']['data'][0]['temperatureMax'], newyork['daily']['data'][0]['temperatureMin'])
else:
    body = "Right now it is {} degrees out and it is {}. Today will be {} with a high of {} and a low of {}. Have a nice day!".format(newyork['currently']['temperature'], newyork['currently']['summary'], newyork['currently']['apparentTemperature'], newyork['daily']['data'][0]['temperatureMax'], newyork['daily']['data'][0]['temperatureMin'])


# In[5]:


import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%B %d,%Y")


# In[6]:


response = requests.post(
        "https://api.mailgun.net/v3/sandbox4bfaef291e9343b1bcd73d6c2179884c.mailgun.org/messages",
        auth=("api", "XXXXXXXXXXXXXXXXXXXX"),
        data={"from": "Foundations Task <mailgun@sandbox4bfaef291e9343b1bcd73d6c2179884c.mailgun.org>",
              "to": ["kelly_kiki@yahoo.gr", "kk3289@columbia.edu"],
              "subject": ("8AM Weather forecast:", date_string),
              "text": body}) 
response.text

