import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)

result = pywapi.google.get_weather('KJFK')

pp.pprint(result)
