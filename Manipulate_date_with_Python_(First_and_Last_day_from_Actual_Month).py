#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Import Library
from datetime import datetime, timedelta, date
import dateutil.relativedelta


# In[5]:


#Code
First_day = "{0}-{1}-01".format(date.today().strftime('%Y'),date.today().strftime('%m')) #First Day from Actual Month like str
Date = date.today() + dateutil.relativedelta.relativedelta(months=1) # Actual day + 1 Month 
d = "{0}{1}01".format(Date.strftime('%Y'),Date.strftime('%m')) # First day next Month
d1 = datetime.strptime(d,"%Y%m%d").date() - timedelta(1) # Last Day from Actual Month like strp
Last_day = d1.strftime("%Y-%m-%d") # Last Day from Actual Month like str

print(First_day)
print(Last_day)

