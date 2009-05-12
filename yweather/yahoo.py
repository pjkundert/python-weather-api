"""
Fetches weather reports from Yahoo! Weather
"""
import urllib2
from xml.dom import minidom

def get_weather(location_id, units = 'metric'):
        """
Fetches weather report from Yahoo!

Parameters 
location_id: A five digit US zip code or location ID. To find your location ID, 
browse or search for your city from the Weather home page(http://weather.yahoo.com/)
The weather ID is in the URL for the forecast page for that city. You can also get the location ID by entering your zip code on the home page. For example, if you search for Los Angeles on the Weather home page, the forecast page for that city is http://weather.yahoo.com/forecast/USCA0638.html. The location ID is USCA0638.

units: type of units. 'metric' for metric and '' for  non-metric
Note that choosing metric units changes all the weather units to metric, for example, wind speed will be reported as kilometers per hour and barometric pressure as millibars.
 
Returns:
weather_data: a dictionary of weather data. See http://developer.yahoo.com/weather/
        """

        WEATHER_URL = 'http://xml.weather.yahoo.com/forecastrss?p=%s&u=%s'
        WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'
        if units == 'metric':
                unit = 'c'
        else:
                 unit = 'f'
        url = WEATHER_URL % (location_id, unit)
        handler = urllib2.urlopen(url)
        dom = minidom.parse(handler)    
        handler.close()
                
        weather_data = {}
        weather_data['title'] = dom.getElementsByTagName('title')[0].firstChild.data
        weather_data['link'] = dom.getElementsByTagName('link')[0].firstChild.data

        ns_data_structure = { 
                'location': ('city', 'region', 'country'),
                'units': ('temperature', 'distance', 'pressure', 'speed'),
                'wind': ('chill', 'direction', 'speed'),
                'atmosphere': ('humidity', 'visibility', 'pressure', 'rising'),
                'astronomy': ('sunrise', 'sunset'),
                'condition': ('text', 'code', 'temp', 'date')

        }       
        
        for (tag, attrs) in ns_data_structure.iteritems():
                weather_data[tag] = xml_get_ns_tag(dom, WEATHER_NS, tag, attrs)

        weather_data['geo'] = {}
        weather_data['geo']['lat'] = dom.getElementsByTagName('geo:lat')[0].firstChild.data
        weather_data['geo']['long'] = dom.getElementsByTagName('geo:long')[0].firstChild.data

        weather_data['condition']['title'] = dom.getElementsByTagName('item')[0].getElementsByTagName('title')[0].firstChild.data
        weather_data['html_description'] = dom.getElementsByTagName('item')[0].getElementsByTagName('description')[0].firstChild.data
        
        forecasts = []
        for forecast in dom.getElementsByTagNameNS(WEATHER_NS, 'forecast'):
                forecasts.append(xml_get_attrs(forecast,('date', 'low', 'high', 'text', 'code')))
        weather_data['forecasts'] = forecasts
        
        dom.unlink()

        return weather_data
        
def xml_get_ns_tag(dom, WEATHER_NS, tag, attrs):
        """
        Parses the necessary tag and returns the dictionary with values
        
        Parameters:
        dom - DOM
        WEATHER_NS - namespace
        tag - necessary tag
        attrs - tuple of attributes

        Returns: a dictionary of elements 
        """
        element = dom.getElementsByTagNameNS(WEATHER_NS, tag)[0]
        return xml_get_attrs(element,attrs)


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
