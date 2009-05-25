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
Fetches weather reports from Google Weather
"""
import urllib2
from xml.dom import minidom

def get_weather(location_id, hl = ''):
        """
        Fetches weather report from Google

        Parameters 
          location_id: a zip code (10001); city name, state (weather=woodland,PA); city name, country (weather=london,england); or possibly others.
          hl: the language parameter (language code)

        Returns:
          weather_data: a dictionary of weather data. 
        """

        WEATHER_URL = 'http://www.google.com/ig/api?weather=%s&hl=%s'
        url = WEATHER_URL % (location_id, hl)
        handler = urllib2.urlopen(url)
        dom = minidom.parse(handler)    
        handler.close()

        weather_data = {}
        weather_dom = dom.getElementsByTagName('weather')[0]

        data_structure = { 
                        'forecast_information': ('city', 'postal_code', 'latitude_e6', 'longitude_e6', 'forecast_date', 'current_date_time', 'unit_system'),
                        'current_conditions': ('condition','temp_f', 'temp_c', 'humidity', 'wind_condition', 'icon')
        }       
        
        forecast_conditions_structure = ('day_of_week', 'low', 'high', 'icon', 'condition')
        for (tag, list_of_tags2) in data_structure.iteritems():
                tmp_conditions = {}
                for tag2 in list_of_tags2:
                        tmp_conditions[tag2] =  weather_dom.getElementsByTagName(tag)[0].getElementsByTagName(tag2)[0].getAttribute('data')
                weather_data[tag] = tmp_conditions

        forecast_conditions = ('day_of_week', 'low', 'high', 'icon', 'condition')

        forecasts = []
        for forecast in dom.getElementsByTagName('forecast_conditions'):
                tmp_forecast = {}
                for tag in forecast_conditions:
                        tmp_forecast[tag] = forecast.getElementsByTagName(tag)[0].getAttribute('data')
                forecasts.append(tmp_forecast)
                weather_data['forecasts'] = forecasts
        
        dom.unlink()

        return weather_data
        

def get_weather_from_google(location_id, hl = ''):
	"""
	Wrapper for get_weather() function.
	"""
	return get_weather(location_id, hl)
	


def xml_get_attrs(xml_element, attrs):
        """
        Returns the list of necessary attributes
        
        Parameters: 
        element: xml element
        attrs: tuple of attributes

        Return: a dictionary of elements
        """
        
        result = {}
        for attr in attrs:
                result[attr] = xml_element.getAttribute(attr)   
        return result
