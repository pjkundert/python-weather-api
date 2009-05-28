import  pywapi
import string

google_result = pywapi.get_weather_from_google('10001')
yahoo_result = pywapi.get_weather_from_yahoo('10001')
noaa_result = pywapi.get_weather_from_noaa('KJFK')
gismeteo_result = pywapi.get_weather_from_gismeteo('72503_1')

print "Google says: It is " + string.lower(google_result['current_conditions']['condition']) + " and " + google_result['current_conditions']['temp_c'] + "C now in New York.\n\n"

print "Yahoo says: It is " + string.lower(yahoo_result['condition']['text']) + " and " + yahoo_result['condition']['temp'] + "C now in New York.\n\n"

print "NOAA says: It is " + string.lower(noaa_result['weather']) + " and " + noaa_result['temp_c'] + "C now in New York."

print "GisMeteo says: It is from" + gismeteo_result['forecasts'][0]['temperature']['min'] + "C to " + gismeteo_result['forecasts'][0]['temperature']['max'] + "C now in New York." 
