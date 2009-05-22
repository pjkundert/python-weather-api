#Copyright (c) 2009 Eugene Kaznacheev <qetzal@gmail.com>

#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:

#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.


"""
Fetches weather reports from Yahoo! Weather
"""
import urllib2
from xml.dom import minidom

def get_weather(station_id):
        """
Fetches weather report from Yahoo!

Parameters 
station_id: http://www.weather.gov/xml/current_obs/seek.php?state=az&Find=Find


Returns:
weather_data: a dictionary of weather data. 
## Icons: http://www.weather.gov/xml/current_obs/weather.php
        """

        WEATHER_URL = 'http://www.weather.gov/xml/current_obs/%s.xml'
        url = WEATHER_URL % (station_id)
        handler = urllib2.urlopen(url)
        dom = minidom.parse(handler)    
        handler.close()
                
        data_structure = ('suggested_pickup',
                                'suggested_pickup_period',
                                'location',
                                'station_id',
                                'latitude',
                                'longitude',
                                'observation_time',
                                'observation_time_rfc822',
                                'weather',
                                'temperature_string',
                                'temp_f',
                                'temp_c',
                                'relative_humidity',
                                'wind_string',
                                'wind_dir',
                                'wind_degrees',
                                'wind_mph',
                                'wind_gust_mph',
                                'pressure_string',
                                'pressure_mb',
                                'pressure_in',
                                'dewpoint_string',
                                'dewpoint_f',
                                'dewpoint_c',
                                'heat_index_string',
                                'heat_index_f',
                                'heat_index_c',
                                'windchill_string',
                                'windchill_f',
                                'windchill_c',
                                'icon_url_base',
                                'icon_url_name',
                                'two_day_history_url',
                                'ob_url'
                                )
	weather_data = {}
        for tag in data_structure:
               weather_data[tag] =  dom.getElementsByTagName('current_observation')[0].getElementsByTagName(tag)[0].firstChild.data

        dom.unlink()
        return weather_data
        



