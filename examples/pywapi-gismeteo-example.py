import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)

result = pywapi.get_weather_from_gismeteo('72503_1')
pp.pprint(result)
