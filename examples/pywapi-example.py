from  pywapi import *
import string

google_result = google.get_weather('10001')
yahoo_result = yahoo.get_weather('10001')
noaa_result = noaa.get_weather('KJFK')

print "Google says: It is " + string.lower(google_result['current_conditions']['condition']) + " and " + google_result['current_conditions']['temp_c'] + "C now in New York.\n\n"

print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "C now in New York.\n\n"

print "NOAA says: It is " + string.lower(noaa_result['weather']) + " and " + noaa_result['temp_c'] + "C now in New York."

