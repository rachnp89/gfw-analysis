# -*- coding: utf-8 -*-
"""
@author: rachaelpetersen

This code utilizes the statsmodel module to run a least-squares regression analysis for tree cover loss time series data at different scales.

"""

import numpy as np
import pandas as pd
from scipy import stats

#SUBNATIONAL UNITS
pnew = pd.read_csv('subnat_loss_percent.csv')
worldperc = pnew.values.tolist()

res = []
for row in worldperc:
    Region = row[0]    
    y = np.array([row[1:]]) # turn tree cover loss time series into an array        
    x = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014])
    slope, intercept, r_value, p_value, stderr = stats.linregress(x,y)
    add = [Region, slope, intercept, r_value**2, p_value, stderr]
    res.append(add)
    
import csv

with open("subnat_accel_results.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(res)

#NATIONAL UNITS
# complete same analysis for national units
pnew = pd.read_csv('nat_loss_percent.csv')
worldperc = pnew.values.tolist()

res = []
for row in worldperc:
    country = row[0]    
    y = np.array([row[1:]]) # turn this into an array        
    x = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014])
    slope, intercept, r_value, p_value, stderr = stats.linregress(x,y)
    add = [country, slope, intercept, r_value**2, p_value, stderr]
    res.append(add)

with open("nat_accel_results.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(res)


#ECOREGION
# complete same analysis, using annual % tree cover loss / extent(2000) as target variable
pnew = pd.read_csv('ecozone_loss_percent.csv')
eco = pnew.values.tolist()

res = []
for row in eco:
    Ecozone = row[0]
    Realm = row[1]    
    y = np.array([row[2:]]) # turn this into an array        
    x = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014])
    slope, intercept, r_value, p_value, stderr = stats.linregress(x,y)
    add = [Ecozone, Realm, slope, intercept, r_value**2, p_value, stderr]
    res.append(add)
    

with open("ecozone_accel_results.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(res)
    
    