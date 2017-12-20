# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 19:48:53 2017

@author: Ken Huang
"""

import pandas as pd
from geopy import geocoders
import threading

def get_lat_lon(address,g,local_var,lat_lon_list):
    '''using Google API to get lat and lon for a list of address'''
    lat = ''
    lon = ''
    local_var.address = address
    local_var.lat = lat
    local_var.lon = lon
    for location in address:
        try:
            lat, lon = g.geocode(location)[-1]
            lat_lon_list.append((location,lat,lon))
        except:
            lat_lon_list.append((location,0,0))


def multi_thread_geocode(address_df,thread_num = 20, key = ''):    
    '''multithreading Google API'''
    if key == '':
        g = geocoders.GoogleV3()
    else:
        g = geocoders.GoogleV3(api_key = key)
    local_var = threading.local()
    lat_lon_list = []
    line = []
    for i in range(thread_num):
        t = threading.Thread(target= get_lat_lon, args=(address_df.iloc[range(i,address_df.shape[0],thread_num)],\
        g,local_var,lat_lon_list), name='Thread-'+str(i))
        line.append(t)
        t.start()
    
    for t in line:
        t.join()    
    
    return lat_lon_list

def batch_geocode(address_df, thread_num = 20, key = ''):
    '''Do geocoding for an address dataframe/list/array, returns a dataframe with columns:
       address,lat,lon.It will take loops to run until no error (timeout etc) exists.'''
    address_df = pd.DataFrame(address_df)
    address_df.columns = ['address']
    address_df = address_df['address']
    address_df = address_df.drop_duplicates()
    temp = pd.DataFrame()
    position_index = 0
    zero_count = [0,0]
    address_lat_lon = multi_thread_geocode(address_df, thread_num, key = key)
    temp['address'],temp['lat'],temp['lon'] = zip(*address_lat_lon)
    z_index = list(temp[temp['lat'] == 0].index)
    zero_count[position_index] = len(z_index)

    while (zero_count[0] != zero_count[1]) & (len(z_index) != 0):
        address_lat_lon = multi_thread_geocode(temp['address'][z_index], thread_num, key = key)
        temp['address'][z_index],temp['lat'][z_index],temp['lon'][z_index] = zip(*address_lat_lon)
        z_index = list(temp[temp['lat'] == 0].index)
        position_index = 1 - position_index
        zero_count[position_index] = len(z_index)
    
    temp.index = temp['address']
    temp = temp.reindex(address_df)
    temp.index = range(temp.shape[0])    
    return temp



