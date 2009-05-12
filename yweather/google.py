"""
Fetches weather reports from Google Weather
"""
import urllib2
from xml.dom import minidom

def get_weather(location_id, hl = ''):
        """
        Fetches weather report from Yahoo!

        Parameters 
          location_id: a zip code (10001); city name, state (weather=woodland,PA); city name, country (weather=london,england); or possibly others.
          hl: the language parameter (language code)

        Returns:
          weather_data: a dictionary of weather data. See http://developer.yahoo.com/weather/
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
                for tag2 in list_of_tags2:
                        weather_data[tag][tag2] =  weather_dom.getElementsByTagName(tag)[0].getElementsByTagName(tag2)[0].getAttribute('data')

        forecast_conditions = ('day_of_week', 'low', 'high', 'icon', 'condition')

        forecasts = []
        for forecast in dom.getElementsByTagName('forecast_conditions'):
                tmp_forecast = {}
                for tag in forecast_conditions.iteritems():
                        tmp_forecast[tag] = forecast.getElementsByTagName(tag).getAttribute('data')
                forecasts.append(tmp_forecast)
                weather_data['forecasts'] = forecasts
        
        dom.unlink()

        return weather_data
        

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
