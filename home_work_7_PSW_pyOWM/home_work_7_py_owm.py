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

#2 Get the ID of a city given its name
registry = owm.city_id_registry()
results = registry.ids_for(city) [0]								# застосовуємо модуль списки для ідентифікації 2ого по списку міста з меню вибору (Philadelphia, PA)

print ("Selected city has the next ID: " + str(results))

#1 Get the current weather status of the city
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

# МЕНЮШКА ВИБОРУ ІНШИХ ПРИХОВАНИХ ПАРАМЕТРІВ ПОГОДНІХ УМОВ:
def add_options():
	wi = w.wind()['deg']                  							# {'speed': 4.6, 'deg': 330}
	hu = w.humidity                									# 87
	tmax = w.temperature('celsius')['temp_max']						# {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0, 'feels_like': 22,68 } - МАСИВ, список одиниць, які викоикаються даною функцією
	tmin = w.temperature('celsius')['temp_min'] 					# вибрали одиницю з даного масиву - а саме параметр ['temp_min']
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

#3 Get geographic coordinates of a city given its name¶

def coords_function():
	list_of_locations = registry.locations_for(city)
	location = list_of_locations[0]									 # ок, в даному випадку це словник, ми виділяємо який саме елемен тми хочемо вибрати з випливаючого списку
	lat = location.lat   											 # широта 
	lon = location.lon   											 # довгота
	print ('Lattitude - ' + str(lat) + ', Longtitude - ' + str(lon)) # не можна конкатенувати дві змнінні int чи float (тому поміщаємо дробні змінні в дужки і конвертуємо в str)


coords_inquiry = input ('Do U want to check geographic coordinations, press Y/N ?: ')
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

#1 Get current weather status on a location¶
print ('Short wetaher status:')
time.sleep(0.75)
print ('...')

mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)  							# the observation object is a box containing a weather object
w = observation.weather 											# general status in the current place
w.status           													# short version of status (eg. 'Rain')
w.detailed_status  													# detailed version of status (eg. 'light rain')
time.sleep(0.75)
print ('...')

#time.sleep(1)
#print (w)       													# w -змінна якій присвоєний результат функції observation weather  (observation у свою чергу містить загальну інформацію - weather at place)

time.sleep(0.75)
print ('In the city of ' + city + ' we have the following weather status: ' + str(w.status))
time.sleep(0.75)
print ('...')
time.sleep(0.75)
print ('Presence of rain∕The force of rain∕Clouds: ' + str(w.detailed_status))

#_______PAUSE______
time.sleep(0.75)
print ('...')
#__________________

#8 Get current pressure on a location
def pressure_function():
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(city)
	pressure_dict = observation.weather.pressure 					# in pyOWM ---weather--- is an inbuilt method
	pressure1 = pressure_dict['press'] 								# press (atmospheric pressure on the ground in hPa)
	pressure2 = pressure_dict['sea_level'] 							# and sea_level (on the sea level, if location is on the sea | discluded from the lsit as a parameter as our locations are on the ground
	time.sleep(0.75)
	print ('...')
	print ('Current atmospheric pressure is ' + str(pressure1) + ' bar∕mPa∕atm')

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

#11 Get today’s sunrise and sunset times for a location

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
	#sunrise_date = weather.sunrise_time(timeformat = 'date')
	
	#sunrise = sunrise_iso.new_timezone_timestamp                   # will add additional timezone to our timezone. doesn't work properly

	sunset_unix = weather.sunset_time() + 10800 # default unit: 'unix'
	#sunset_iso = weather.sunset_time(timeformat='iso')
	sunset_local = pyowm.utils.formatting.timeformat(sunset_unix, 'iso')
	#sunset_date = weather.sunset_time(timeformat = 'date')

	print (f'Today’s sunrise time is - {sunrise_local}. Today\'s sunset time is∕will be - {sunset_local}' )
	# print (str(sunrise_local)+ ' ' + str(sunset_local))
	
	# ВІДФОРМАТУВАТИ ДАНІ БЕЗ +00 ТА БЕЗ ДАТИ
	

sunrise_inquiry = input ('Do U want to check today’s sunrise and sunset times, press Y/N ?: ')
yeslist = ['Y', 'yes', 'Yes']

if pressure_inquiry in yeslist:
	time.sleep(0.75)
	print ('...')
	sunrise_function()
if not pressure_inquiry in yeslist:
	pass

#7 Get current rain amount on a location
rain_inquiry = input ('Do U want to check the amount of fallen rain?: ')

def rain_function():
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(city)
	rain_dict = observation.weather.rain                                
	print (str(rain_dict))
	# rr = rain_dict['3h']  #------------------------------------------error
	# print (r)
	#print ('Current amount of rain is: ' + str(r) + ' mm')

yeslist = ['Y', 'yes', 'Yes']

if rain_inquiry in yeslist:
	time.sleep(0.75)
	rain_function()
if not rain_inquiry in yeslist:
	pass

time.sleep(0.75)
print ('...')

print ('Thank you for using pyowm')
