from tkinter import *
from configparser import ConfigParser
import requests
import tkinter as tk
from PIL import Image, ImageTk

import pyowm.owm
from pyowm.owm import OWM

owm = OWM('8387b7e23ef87eb351bc3497d07a6dbc')

#url = 'https://api.openweathermap.org/data/2.5/weather'

# config_file = 'config.ini'
# config = ConfigParser()
# config.read(config_file)
# api_key = config ['api_key']['key']

api_key = '8387b7e23ef87eb351bc3497d07a6dbc'

############ doesn't work ### could not get json data from owm

# def get_weather(city):
#     result = requests.get(url.format(city, api_key))
#     if result:
#         json = result.json()
#         city = json ['name']
#         country = json ['sys'] ['country']
#         temp_kelvin = json ['main'], ['temp']
#         temp_fahrenheit = ((temp_kelvin - 273.15) * 9 / 5 + 32)
#         icon = json ['weather'][0]['main']
#         weather = json ['weather'][0]['main']
#         total = (city, country, temp_celsius, temp_fahrenheit, icon, weather_)
#         return total
#     else:
#         return None
# print (get_weather(city))

############ doesn't work ### could not get json data from owm

#1 GET A CURRENT WEATHER STATUS OF THE CITY

def get_weather(city): # main class
	
	# owm block
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(city)
	w = observation.weather

	# get_short_weather_status
	sh_status = w.status           								# short version of status (eg. 'Rain')
	det_status = w.detailed_status  							# detailed version of status (eg. 'light rain')

	# get_id_city
	registry = owm.city_id_registry()
	id_result = registry.ids_for(city) [0]

	# get_weather_options
	wi = w.wind() ['speed']
	hu = w.humidity
	tmax = w.temperature('celsius')['temp_max']
	tmin = w.temperature('celsius')['temp_min']
	t_feel = w.temperature('celsius')['feels_like']
		
	# get_pressure
	pressure_dict = observation.weather.pressure 				# in pyOWM ---weather--- is an inbuilt method
	pressure1 = pressure_dict['press'] 							# press (atmospheric pressure on the ground in hPa)
	pressure2 = pressure_dict['sea_level']

	# get coords
	list_of_locations = registry.locations_for(city)
	location = list_of_locations[0]								# list of locatins - dictionary # will get allways 1'st by default
	lat = round((location.lat), 2) 								
	lon = round((location.lon), 2)
	
	# get sunrise & sunset
	sunrise_unix = w.sunrise_time() + 10800 					#it's 10800 seconds = 3 hours # default unit: 'unix'											 					 
	sunrise_local = (pyowm.utils.formatting.timeformat(sunrise_unix, 'iso'))[10:-3]																 

	sunset_unix = w.sunset_time() + 10800 # default unit: 'unix'
	sunset_local = (pyowm.utils.formatting.timeformat(sunset_unix, 'iso' ))[10:-3]

	# get rain for the last 1-12 hours (depends on meteo json response)
	rain_dict = observation.weather.rain                               

	final = (wi, hu, tmax, tmin, t_feel, pressure1, pressure2, id_result, lat, lon, sunrise_local, sunset_local, rain_dict, sh_status, det_status)                     											# <Weather - reference time=2013-12-18 09:20, status=Clouds>     
	return (final)

#### 

def get_short_status(): # дочірній клас
	city = city_text.get()
	weather = get_weather(city)
	try:
		location_lbl['text'] = (f'Weather status: {weather[13]}. Precipitation: {weather[14]} ')
		image ['bitmap'] = 'images/{}.png'.format(weather[13])
		temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
	except:
		print ('Error', 'Cannot find such city{}'.format(city))

def get_id_city():
	city = city_text.get()
	weather = get_weather(city)
	
	try:
		location_lbl['text'] = (f'City ID: {weather[7]}')
		image ['bitmap'] = 'images/{}.png'.format(weather[4])
		temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
	except:
		print ('Error', 'Cannot find such city{}'.format(city))

def get_weather_options(): 
	city = city_text.get()
	weather = get_weather(city)

	try:
		location_lbl['text'] = (f'Clouds: {weather[13]}')
		temp_lbl['text'] = (f'Tmax {weather[2]} °C |  Tmin {weather[3]} °C | feels-like T {weather[4]} °C')
		weather_lbl['text']= (f'Wind: {weather[0]} m∕s | Humidity {weather[1]} %')
		image ['bitmap'] = 'images/{}.png'.format(weather[4])
	except:
		print ('Error', 'Cannot find such city{}'.format(city))


def get_pressure(): 
	city = city_text.get()
	pressure = get_weather(city)
	
	try:	
		location_lbl['text'] = (f'{pressure[5]} bar∕mPa∕atm ')	
		image['bitmap'] = 'images/{}.png'
		temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(pressure[2], pressure[3])
	except:
		print ('Error', 'Cannot find such city{}'.format(city))

def get_coords():
	city = city_text.get()
	coords = get_weather(city)

	try:	
		location_lbl['text'] = (f'Lat: {coords[8]} Lon: {coords[9]}')	
		image['bitmap'] = 'images/{}.png'
		temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(coords[2], coords[3])
	except:
		print ('Error', 'Cannot find such city{}'.format(city))

def get_sunrise(): 
	city = city_text.get()
	sunrise = get_weather(city)

	try:	
		location_lbl['text'] = (f'Sunrise time: {sunrise[10]}s Sunset time: {sunrise[11]}s')	
		image['bitmap'] = 'images/{}.png'
		temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(sunrise[2], sunrise[3])
	except:
		print ('Error', 'Cannot find such city{}'.format(city))

def get_rain():
	city = city_text.get()
	rain = get_weather(city)

	try:
		rr = rain[12]['1h']
		#location_lbl['text'] = (f'{rr}')
		location_lbl['text'] = (f'Last {str(rr)[2:3]} hour: {str(rr)[-5:-1]}mm') ## shift the key in 214 from 1h to (n)h !! not all cities possess other keys than '1h'	
	except KeyError as err:
		error_lbl['text'] = ('Ooops. There is no sufficient amount of rain to determine', err)
	except:
		print ('Error', 'Cannot find such city{}'.format(city))

# one_call data (forecast for the next day)
def get_one_call():
    city = tom_forecast_city.get()
    
    mgr = owm.weather_manager()
    registry = owm.city_id_registry()
    list_of_locations = registry.locations_for(city)
    
    location = list_of_locations[0]								# list of locatins - dictionary # will get allways 1'st by default
    lat = round((location.lat), 2) 								
    lon = round((location.lon), 2)
    
    one_call = mgr.one_call(lat, lon)

    tom_temp = one_call.forecast_daily[0].temperature('celsius').get('feels_like_morn', None)
    tom_wi = one_call.forecast_hourly[6].wind().get('speed', 0)
    tom_hu = one_call.forecast_hourly[6].humidity

    try:
	    location2_lbl['text'] = (f'Feels like morning T: {tom_temp}°C.\n\
        Wind: {tom_wi} m∕s. \n\
        Humidity: {tom_hu} %')
	    #image['bitmap'] = 'images/{}.png'
	    #temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(coords[2], coords[3])
    except:
        print ('Error', 'Cannot find such city{}'.format(city))


##############################################################################################
# tkinter GUI

app = Tk() # create a an app Variable                                                                                                                                                                                                           

app.title ('WEATHER APP')

app.geometry('500x650') #1000 width 400 height

###############################################################################################

##### search window#1 parameters # це меню вводу параметрів

space2_lbl = Label(app, text='', font=('bold', 15), height = 4)
space2_lbl.pack()

##### search window#1 parameters # це меню вводу параметрів

city_text = StringVar()
city_entry = Entry(app, justify = CENTER, width = 44, textvariable=city_text)
city_entry.pack() # pack function - place a button on the screen (pack() is a placing function)

###############################################################################################

###### Вивід статусу інформації відповідно до міста
location_lbl = Label(app, text='Location', font=('bold', 15), bg='#a6aab0')
location_lbl.pack()

# button#1 get_id
search_btn = Button (app, text = 'Check ID', width=40, command=get_id_city)
search_btn.pack() 

# button#2 get_short_status
search_btn7 = Button (app, text = 'Short Weather Status', width=40, command=get_short_status)
search_btn7.pack()

# button#3 get_weather_options
search_btn2 = Button (app, text = 'Detailed Weather Status', width=40, command=get_weather_options)
search_btn2.pack() 

# button#4 get_pressure
search_btn3 = Button (app, text = 'Check Pressure', width=40, command=get_pressure)
search_btn3.pack()

# button#5 get_coords
search_btn4 = Button (app, text = 'Check Coords', width=40, command=get_coords)
search_btn4.pack()

# button#6 get_sunrise_
search_btn5 = Button (app, text = 'Check Sunrise∕Sunset', width=40, command=get_sunrise)
search_btn5.pack()

# button#7 get_rain
search_btn6 = Button (app, text = 'Check Rain Amount', width=40, command=get_rain)
search_btn6.pack()

###### Статус програми
error_lbl = Label(app, text='Program Status: OK', font=('bold', 10))
error_lbl.pack()

###### Статус картинки - не працює
image = Label(app, bitmap='')
image.pack()

####### Статус температури
temp_lbl = Label(app, text='temperature')
temp_lbl.pack()

###### Статус погоди
weather_lbl = Label(app, text='weather')
weather_lbl.pack()


###### Пробіл між кнопками
space_lbl = Label(app, text='', font=('bold, 20'))
space_lbl.pack()

####### Погода завтра вранці                                                                                                                                                                                                
tom_forecast_city = StringVar()
forecast_entry = Entry(app, width=42, textvariable=tom_forecast_city)
forecast_entry.pack() # tomorrow mornings weather

####### прогноз стрічка
location2_lbl = Label(app, text='Location', font=('bold', 15), bg='#a6aab0')
location2_lbl.pack()

####### прогноз стрічка
# button#8 forecast_for_tomorrow
forecast_btn = Button (app, text = 'Tomorrow Forecast', width=40, command=get_one_call)
forecast_btn.pack()

######################3
#іконка


#app = Tk()
#root.geometry("550x300+300+150")
#app.resizable(width=True, height=True)

img  = Image.open("/home/netunit/Стільниця/Soft/Project_LV-527/weather_app/images/11d@2x.png") 
photo=ImageTk.PhotoImage(img)
#img = img.resize(100, 100, '11n@2x.png')
lab=Label(image=photo).place(x=0,y=0)


####################3
### іконка в меню - не працює
#app.iconbitmap('/home/netunit/Стільниця/Soft/Project LV-527/myproject/images∕Cloudy_Rain.ico')
                                                                                                                                                                                                                                                                                         
#app = tk.Tk()
#app.tk.call('wm', 'iconphoto', app._w, tk.PhotoImage(file='/home/netunit/Стільниця/Soft/Project LV-527/myproject/venv∕tmp.png'))

# app = tk.Tk()

# app.iconphoto(False, tk.PhotoImage(file='/home/netunit/Стільниця/Soft/Project LV-527/myproject/venv∕tmp.png'))
# app.mainloop()

app.mainloop() # function to create the main window
