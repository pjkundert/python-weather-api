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
