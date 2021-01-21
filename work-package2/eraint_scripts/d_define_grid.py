# -*- coding: utf-8 -*-
"""
@author: DAVID + Michael
"""
import pandas as pd

##########################
# define a coordinate class
##########################
class Coordinate:
    """Define a coordinate class"""
    
    def __init__(self, Longitude, Latitude):
        self.Longitude = Longitude
        self.Latitude = Latitude

    def __str__(self):
        """Returns a string representation of self"""
        return "<" + str(self.Longitude) + "," + str(self.Latitude) + ">"

    def getgrids(self, delta):
        """
        subsets the grid points up to delta distance
        away around the tide gauge - delta is in degrees
        """
        lonmax = self.Longitude + delta
        if lonmax > 360:
            lonmax = lonmax - 360
        elif lonmax < 0:
            lonmax = lonmax + 360
        lonmin = self.Longitude - delta
        if lonmin < 0:
            lonmin = lonmin + 360
        latmax = self.Latitude + delta
        latmin = self.Latitude - delta
        return (lonmin, lonmax), (latmin, latmax)


##########################
# find closest grid points
##########################
def findPixels(tg_cord, delta, lon, lat):
    """
    this function subsets lon and lat grid points within the 
    specified distance delta (in degrees)
    """
    lon_margin = tg_cord.getgrids(delta)[0]
    lat_margin = tg_cord.getgrids(delta)[1]

    lonlat = [];
    # getting the grids from the nc file
    long = lon
    latt = lat

    #account for negative values of tg lon - to match that of the netcdfs
    if lon_margin[0] > lon_margin[1]:
        part1 = long[(long[0] > lon_margin[0]) & (long[0] < 360)]
        part2 = long[(long[0] >= 0) & (long[0] < lon_margin[1])]
        lon_sub = pd.concat([part1, part2], axis = 0)
    else:
        lon_sub = long[(long[0] > lon_margin[0]) & (long[0] < lon_margin[1])]
        
        
    lat_sub = latt[(latt[0] > lat_margin[0]) & (latt[0] < lat_margin[1])]

    #print(lon_sub)
    #print(lat_sub)

    for ii in lon_sub[0]:
        for jj in lat_sub[0]:
            current = Coordinate(ii, jj)
            lonlat.append(current)

    return lonlat


######################################################
# find indices of lon & lat of the closest grid points
######################################################
def findindx(point, lon, lat):
    """Finds the lon/lat index for the given grid point
       point is a coordinate class
    """
      
    lonind = []; latind = []
    for ii in range(len(point)):
        lonind.append(lon[lon[0] == point[ii].Longitude].index.item())
        latind.append(lat[lat[0] == point[ii].Latitude].index.item())
    return pd.DataFrame([lonind, latind]).T