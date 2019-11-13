#JSON parser
#Purpose: Allow a user to interactivly select JSON or geoJson data and convert it in a way
# to select important features, if needed
# so what I need from the Openstreetmap is  CUISINE, NAME, GEOM:COORDINATES
import json
import re
import string
import numpy as np
import pandas as pd

#-----------------code------------#
# had to over ride the data and this is a good refresher on dictionaries in pyhton



my_list = []
my_holder = []
id_count = 0

with open('NVA_rest.JSON','r', encoding='utf8', errors='ignore') as file:
    data = json.loads(file.read())

for features in data['features']:
    #iterates the properites in  features

    # checks to see if the field has cuisine the name, need both not just random stuff
    # the data does not have input standards
    if('cuisine' in features['properties']):
        if('name' in features['properties']):
            my_holder.append(id_count)
            id_count += 1
            for index in features['properties']:
                
                # iterates into the values that I need
                if index == 'cuisine':
                    my_holder.append(features['properties'][index])
        
                elif index == 'name':
                    my_holder.append(features['properties'][index])
    
            for index2 in features['geometry']:
        # iterates the geometry
                if index2 == 'coordinates':
            #long lat formation
            #print(features['geometry'][index2][0])
                    my_holder.append(features['geometry'][index2][1])
                    my_holder.append(features['geometry'][index2][0])
            my_list.append(my_holder)
            my_holder = []
    # if 'cuisine' can't be found, then just skip the record
    else:
        continue
        
    
    
    
   
df = pd.DataFrame(my_list, columns = ['ID','CUISINE','NAME','LAT','LON'])

df.to_csv('D:/My_project/GeoJSON_data/cleaned_data.csv', index = False, header = True)






