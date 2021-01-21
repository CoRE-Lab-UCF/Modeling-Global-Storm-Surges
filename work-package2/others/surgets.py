# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:12:10 2019

@author: Michael Tadesse 
"""

import datetime
import pandas as pd

def add_date(ts):
    """
    concatenates the separated dates to get a datetime 
    for each row of the surge value
    ts : the hourly time series surge values
    """
    date_part = ts.loc[:,2:7] #extract time columns
    #convert to list for ease of lambda operation
    date_part_list = date_part.values.tolist() 
    convertor = lambda x: datetime.datetime(x[0],x[1],x[2],x[3],x[4],x[5])
    date_final = pd.DataFrame(map(convertor, date_part_list))
    
    ts['date'] = date_final
    
    return ts