import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)

result = pywapi.get_weather_from_google('10001')

pp.pprint(result)
