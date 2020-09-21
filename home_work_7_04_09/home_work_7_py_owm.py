#https://youtu.be/53GBGBcMS6I - PyPi - HowdyHo

import pyowm.owm
from pyowm.owm import OWM
owm = OWM('8387b7e23ef87eb351bc3497d07a6dbc')
import time
import datetime
import pytz

#_______LOADING______
time.sleep(0.75)
print ('....')
time.sleep(0.75)
print ('...Loading...')
time.sleep(0.75)
print ('....')
time.sleep(0.75)
#__________________

city = input ('What city do U want to check the weather in?: ')

time.sleep(0.75)

#2 GET THE ID OF A CITY GIVEN IT'S NAME

registry = owm.city_id_registry()
results = registry.ids_for(city) [0]								# застосовуємо модуль списки для ідентифікації 2ого по списку міста з меню вибору (Philadelphia, PA)

print ("Selected city has the next ID: " + str(results))

#1 GET A CURRENT WEATHER STATUS OF THE CITY

mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
# print(w)                											# <Weather - reference time=2013-12-18 09:20, status=Clouds>

# Weather details
wi = w.wind() ['speed']                 							# {'speed': 4.6, 'deg': 330}
hu = w.humidity                										# 87
t = w.temperature('celsius') ['temp'] 								# {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0, 'feels_like': 22,68 }

print ("In the city of " + city + ", we have the next weather conditions: " + "Wind speed - " + str(wi) + " km∕h" + ", relative humidity - " + str(hu) + "% " + ", T - " + str(t) + " °C")

#_______PAUSE______
time.sleep(0.75)
print ('...')
#__________________

# 1.1 OPTIONS FOR OTHER ADDITIONAL WEATHER PARAMETERS(TEMP MIN, TEMP MAX, WIND SPEED, FEEL'S LIKE T, WIND ANGLE):

def add_options():
	wi = w.wind()['deg']                  							# {'speed': 4.6, 'deg': 330}
	hu = w.humidity                									# 87
	tmax = w.temperature('celsius')['temp_max']						# {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0, 'feels_like': 22,68 } - data cortege that this function returns
	tmin = w.temperature('celsius')['temp_min'] 					# get ['temp_min'] key - to get Tmin parameter from the dict
	t_feel = w.temperature('celsius')['feels_like']
	
	detailed_w = input ('More info here, press Y/N ?: ')	
	yeslist = ['Y', 'yes', 'Yes']

	if detailed_w in yeslist:
		time.sleep(0.75)
		print ('...')
		time.sleep(0.75)
		print ("Other weather rates: wind angle - " + str(wi) + '° ' + ", max T - " + str(tmax) + " °C" + ", min T - " + str(tmin) + " °C" + ", feels like T - " + str(t_feel) + " °C")
	if not detailed_w in yeslist: 
		pass

add_options() 														# running a function with additional options

#_______PAUSE______
time.sleep(0.75)
print ('...')
#__________________

#3 GET THE GEOGRAPHIC COORDS OF THE CITY GIVEN IT'S NAME¶

def coords_function():
	list_of_locations = registry.locations_for(city)
	location = list_of_locations[0]									 # ок, в даному випадку це словник, ми виділяємо який саме елемен тми хочемо вибрати з випливаючого списку
	lat = location.lat   											 # широта 
	lon = location.lon   											 # довгота
	print ('Lattitude - ' + str(lat) + ', Longtitude - ' + str(lon)) # не можна конкатенувати дві змнінні int чи float (тому поміщаємо дробні змінні в дужки і конвертуємо в str)


coords_inquiry = input ('Do U want to check geographic coordinates, press Y/N ?: ')
yeslist = ['Y', 'yes', 'Yes']

if coords_inquiry in yeslist:
	time.sleep(0.75)
	print ('...')
	time.sleep(0.75)
	coords_function()
else:
	pass

#_______PAUSE______
time.sleep(0.75)
print ('...')
#__________________

#4 GET A CURRENT WEATHER STATUS ON A LOCATION

print ('Short weather status:')
time.sleep(0.75)
print ('...')

mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)  							# the observation object is a box containing a weather object
w = observation.weather 											# general status in the current place
w.status           													# short version of status (eg. 'Rain')
w.detailed_status  													# detailed version of status (eg. 'light rain')

#time.sleep(1)
#print (w)       													# w -змінна якій присвоєний результат функції observation weather  (observation у свою чергу містить загальну інформацію - weather at place)

time.sleep(0.75)
print ('In the city of ' + city + ' we have the following weather status: ' + str(w.status))
time.sleep(0.75)
print ('Presence of rain∕The force of rain∕Clouds: ' + str(w.detailed_status))

#_______PAUSE______
time.sleep(0.75)
print ('...')
#__________________

#5 GET A CURRENT PRESSURE ON A LOCATION

def pressure_function():
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(city)
	pressure_dict = observation.weather.pressure 					# in pyOWM ---weather--- is an inbuilt method
	pressure1 = pressure_dict['press'] 								# press (atmospheric pressure on the ground in hPa)
	pressure2 = pressure_dict['sea_level'] 							# and sea_level (on the sea level, if location is on the sea | discluded from the lsit as a parameter as our locations are on the ground
	time.sleep(0.75)
	print ('...')
	print ('Current atmospheric pressure is: ' + str(pressure1) + ' bar∕mPa∕atm')

pressure_inquiry = input ('Do U want to check the atmospheric pressure, press Y/N ?: ')
yeslist = ['Y', 'yes', 'Yes']

if pressure_inquiry in yeslist:
	time.sleep(0.75)
	print ('...')
	pressure_function()
if not pressure_inquiry in yeslist:
	pass

#_______PAUSE______
time.sleep(0.75)
print ('...')
#__________________

#6 GET TODAY'S SUNRISE AND SUNSET TIMES FOR A LOCATION

# a timestamp I'd like to convert
#my_timestamp = datetime.datetime.now()
#print (my_timestamp)

# create both timezone objects
# old_timezone = pytz.timezone('Europe/London')
# new_timezone = pytz.timezone('Europe/Kiev')

# two-step process
# localized_timestamp = old_timezone.localize(my_timestamp)
# new_timezone_timestamp = localized_timestamp.astimezone(new_timezone)
# print (new_timezone_timestamp)

#______________________________CONVERTATION TO CURRENT TIMEZONE _________________________#don't work

### ASK LIYBOV KOLIASA HOW TO WORK WITH TIME ## CONVERT TIME 'ISO', 'UNIX' 

def sunrise_function():
	observation = mgr.weather_at_place(city)
	weather = observation.weather

	sunrise_unix = weather.sunrise_time() + 10800 					#it's seconds 10800 seconds = 3 hours # default unit: 'unix'
	#sunrise_iso = weather.sunrise_time(timeformat='iso') #Greenwich time 
	sunrise_local = pyowm.utils.formatting.timeformat(sunrise_unix, 'iso') # converting time instructions: http://joxi.net/DmBb187T48nEam
	#print (sunrise_local)
	#sunrise_date = weather.sunrise_time(timeformat = 'date')
	
	#sunrise = sunrise_iso.new_timezone_timestamp                   # will add additional timezone to our timezone. doesn't work properly

	sunset_unix = weather.sunset_time() + 10800 # default unit: 'unix'
	#sunset_iso = weather.sunset_time(timeformat='iso')
	sunset_local = pyowm.utils.formatting.timeformat(sunset_unix, 'iso' )
	#print (type(sunset_local))
	#sunset_date = weather.sunset_time(timeformat = 'date')

	print (f'Today’s sunrise time: {(sunrise_local)[10:-3]}sec. Today\'s sunset time: {(sunset_local)[10:-3]}sec' )
	# print (str(sunrise_local)+ ' ' + str(sunset_local))
	
	# ВІДФОРМАТУВАТИ ДАНІ БЕЗ +00 ТА БЕЗ ДАТИ
	

sunrise_inquiry = input ('Do U want to check today’s sunrise and sunset times, press Y/N ?: ')
yeslist = ['Y', 'yes', 'Yes']

if sunrise_inquiry in yeslist:
	time.sleep(0.75)
	print ('...')
	sunrise_function()
if not sunrise_inquiry in yeslist:
	pass

#_______PAUSE______
time.sleep(0.75)
print ('...')
#__________________

#7 GET CURRENT RAIN AMOUNT ON A LOCATION

yeslist = ['Y', 'yes', 'Yes']
rain_inquiry = input ('Do U want to check the amount of fallen rain?: ')

def rain_function():
	try:
		mgr = owm.weather_manager()
		observation = mgr.weather_at_place(city)
		rain_dict = observation.weather.rain                               
		rr = rain_dict['1h'] # data cortege  ## it's better to select Megapolises, as their meteo works much better
		print (f'Current amount of rain fallen for the last {str(rr)[2:3]} hour: {str(rr)[-5:-1]}mm') ## shift the key in 214 from 1h to (n)h !! not all cities possess other keys than '1h'
	
	except KeyError as err:
		print ('Ooops. There is no sufficient amount of rain to determine')

if rain_inquiry in yeslist:
	time.sleep(0.75)
	rain_function()
if not rain_inquiry in yeslist:
	pass

	#_______PAUSE______
time.sleep(0.75)
print ('...')
#__________________

#8 'ONE CALL' DATA - GETTING A FORECAST FOR TOMORROW (FEEL'S LIKE T, WIND SPEED, )

def one_call():
	list_of_locations = registry.locations_for(city)
	location = list_of_locations[0]									 # в даному випадку це словник, ми виділяємо який саме елемен тми хочемо вибрати з випливаючого списку
	lat = location.lat   											 # широта 
	lon = location.lon

	one_call = mgr.one_call(lat, lon)
	tom_temp = one_call.forecast_daily[0].temperature('celsius').get('feels_like_morn', None)
	tom_wi = one_call.forecast_hourly[6].wind().get('speed', 0)
	tom_hu = one_call.forecast_hourly[6].humidity
	
	#tom_w = one_call.forecast_daily[0].w
	
	time.sleep(0.75)
	print ('Short weather status for tomorrow morning, 9 am: ')
	time.sleep(0.75)

	print ((f'Feels like morning T: {(tom_temp)} °C. Morning wind speed: {tom_wi} m∕s. Relative humidity: {tom_hu} %')) #Ex.: 7.7
	
	#print ('Feels like morning T: ' + str(tom_temp) + ' °C' ) #Ex.: 7.7
	#print( 'Morning wind speed: ' + str (tom_wi) + 'm∕s')
	#print( 'Relative humidity: ' + str (one_call.forecast_hourly[6].humidity) + '%')
	#print( 'Relative humidity: ' + str (one_call.forecast_hourly[6].humidity) + '%')

def yes_no():
	call_inquiry = input ('Do U want to check tomorrow morning\'s weather: ')
	
	yeslist = ['Y', 'yes', 'Yes']

	if call_inquiry in yeslist:
		time.sleep(0.75)
		one_call()
	if not call_inquiry in yeslist:
		pass
yes_no()


time.sleep(0.75)
print ('...')

print ('Thank you for using pyowm :) ')

# in total - 8 parameters