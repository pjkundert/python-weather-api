"""
Fetches weather reports from Yahoo! Weather
"""


def get_weather(location_id):
	"""
Fetches weather report from Yahoo!

Parameters 
location_id: a zip code (10001); city name, state (weather=woodland,PA); city name, country (weather=london,england); or possibly others.

Returns:
weather_data: a dictionary of weather data. See http://developer.yahoo.com/weather/
	"""

	WEATHER_URL = 'http://www.google.com/ig/api?weather=%s'
	url = WEATHER_URL % (location_id)
	handler = urllib2.urlopen(url)
	dom = minidom.parse(handler)	
	handler.close()

	#	weather_data = {}
	#	weather_data['title'] = dom.getElementsByTagName('title')[0].firstChild.data

	#	ns_data_structure = { 
	#		'location': ('city', 'region', 'country'),
	#		'units': ('temperature', 'distance', 'pressure', 'speed'),
	#		'wind': ('chill', 'direction', 'speed'),
	#		'atmosphere': ('humidity', 'visibility', 'pressure', 'rising'),
	#		'astronomy': ('sunrise', 'sunset'),
	#		'condition': ('text', 'code', 'temp', 'date')
	#
	#	}	
	
	#	for (tag, attrs) in ns_data_structure.iteritems():
	#		weather_data[tag] = xml_get_ns_tag(dom, WEATHER_NS, tag, attrs)

	#	forecasts = []
	#	for forecast in dom.getElementsByTagNameNS(WEATHER_NS, 'forecast'):
	#	        forecasts.append(xml_get_attrs(forecast,('date', 'low', 'high', 'text', 'code')))
	#	weather_data['forecasts'] = forecasts

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
