# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 12:11:13 2020

To filter metric data spatially
filter metric using lon and lat
then plot a hstogram 

@author: Michael Tadesse
"""

#assign dat with desired metric file

westCoast = dat[(dat['lon'] >= -180) & (dat['lon'] <= -120) 
                    & (dat['lat'] >= 30) & (dat['lat'] <= 62)]

eastCoast = dat[(dat['lon'] >= -83) & (dat['lon'] <= -50) 
                    & (dat['lat'] >= 25) & (dat['lat'] <= 45)]

europe = dat[(dat['lon'] >= -20) & (dat['lon'] <= 40) 
                    & (dat['lat'] >= 30) & (dat['lat'] <= 70)]

japan = dat[(dat['lon'] >= 128) & (dat['lon'] <= 150) 
                    & (dat['lat'] >= 30) & (dat['lat'] <= 45)]

seAsia = dat[(dat['lon'] >= 95) & (dat['lon'] <= 180) 
                    & (dat['lat'] >= -12) & (dat['lat'] <= 10)]

oceania = dat[(dat['lon'] >= 115) & (dat['lon'] <= 180) 
                    & (dat['lat'] >= -60) & (dat['lat'] <= -10)]

#count
westCoast['Reanalysis'].value_counts()