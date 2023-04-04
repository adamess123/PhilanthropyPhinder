import pandas as pd
import math as m
from ast import literal_eval
import os as os

from geopy.geocoders import Nominatim
def haversine(latlon1, latlon2):
    latlon1 = literal_eval(latlon1)
    lat1 = latlon1[1]
    lon1 = latlon1[0]
    lat2 = latlon2[1]
    lon2 = latlon2[0]
    radius = 6371  # radius of the Earth in km
    lat_diff = m.radians(lat2 - lat1)
    long_diff = m.radians(lon2 - lon1)
    lat1 = m.radians(lat1)
    lat2 = m.radians(lat2)

    a = m.sin(lat_diff/2) * m.sin(lat_diff/2) + m.cos(lat1) * m.cos(lat2) * m.sin(long_diff/2) * m.sin(long_diff/2)
    c = 2 * m.atan2(m.sqrt(a), m.sqrt(1-a))
    d = radius * c
    d /= 1.609
    d = round(d, 2)
    return d

def search(street, city, state, zip, ntee_id):
    geolocator = Nominatim(user_agent="User Locator")
    user_loc = street + ', ' + city + ', ' + state + ', ' + zip
    user_location = geolocator.geocode(user_loc)
    if user_location is None:
        user_loc = city + ', ' + state
        user_location = geolocator.geocode(user_loc)
    if user_location is None:
        return pd.DataFrame(columns=['NAME', 'Location', 'lat_lon', 'dist'])
    user_lat_lon = (user_location.longitude, user_location.latitude)
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, f'{state}.csv')
    state_df = pd.read_csv(filename)
    state_df = state_df.loc[state_df['Category'] == ntee_id]
    state_df['dist'] = state_df['lat_lon'].apply(lambda x: haversine(x, user_lat_lon))
    state_df = state_df.drop(['NTEE_CD', 'Category', 'lat_lon'], axis=1)
    result = state_df.sort_values(by=['dist'])
    result = result.head(100)
    return result
