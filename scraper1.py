def top_schools():
#     import packages
    import pandas as pd
    import numpy as np
    from bs4 import BeautifulSoup
    import requests
    import sys
    import time
    time.sleep(5)
    from geopy.distance import geodesic
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="ameliadahm@gmail.com")
  
    page = requests.get("https://www.publicschoolreview.com/washington/king-county")
    
    soup = BeautifulSoup(page.content, 'html.parser')

    school_name = []
    for item in soup.find_all(class_='tooltip'):
        item = item.text
        if not item.endswith(')'): # ends with ) means school is closed
            school_name.append(item)
            
    address = []
    for item in soup.find_all(class_='table_cell_county'):
        item = item.text[:-14]
        address.append(item.strip())
    for item in address:
        if item == '':
            address.remove(item)
    address = address[:35]
    
    latitude = []
    longitude = []
    for item in address:
        location = geolocator.geocode(item)
        if location != None:
            latitude.append(location.latitude) 
            longitude.append(location.longitude)
        else:
            latitude.append(np.NaN) 
            longitude.append(np.NaN)
            
    school_coordinates = [{'name': a, 'lat': b, 'long': c, 'ad': d} for (a, b, c, d) in zip(school_name, latitude, longitude, address)]
    
    school_coordinates = pd.DataFrame.from_dict(school_coordinates)
    
    school_coordinates.at[3, 'lat'] = 47.645720
    school_coordinates.at[3, 'long'] = -122.035450

    school_coordinates.at[9, 'lat'] = 47.649000
    school_coordinates.at[9, 'long'] = -122.112320

    school_coordinates.at[10, 'lat'] = 47.640370
    school_coordinates.at[10, 'long'] = -122.173700

    school_coordinates.at[12, 'lat'] = 47.572090
    school_coordinates.at[12, 'long'] = -122.220080

    school_coordinates.at[13, 'lat'] = 47.532190
    school_coordinates.at[13, 'long'] = -122.228770

    school_coordinates.at[14, 'lat'] = 47.685810
    school_coordinates.at[14, 'long'] = -122.032990

    school_coordinates.at[16, 'lat'] = 47.716310
    school_coordinates.at[16, 'long'] = -122.230710

    school_coordinates.at[20, 'lat'] = 47.645720
    school_coordinates.at[20, 'long'] = -122.035450

    school_coordinates.at[21, 'lat'] = 47.755040
    school_coordinates.at[21, 'long'] = -122.080570

    school_coordinates.at[26, 'lat'] = 47.604650
    school_coordinates.at[26, 'long'] = -122.198440

    school_coordinates.at[32, 'lat'] = 47.691960
    school_coordinates.at[32, 'long'] = -122.114210

    school_coordinates.at[34, 'lat'] = 47.655850
    school_coordinates.at[34, 'long'] = -122.338010


    return school_coordinates