import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)

location = 'RSXX0199'
result = pywapi.get_weather_from_yahoo(location, 'metric')

pp.pprint(result)

