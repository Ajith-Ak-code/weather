import requests
import json

data=requests.get('https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22')
date_component=[]

date_input,time_input=data.json()['list'][0]['dt_txt'].split(' ')

def temp():
	temps=data.json()['list'][0]['main']['temp']
	print(temps)
def wind():
	winds=data.json()['list'][0]['wind']['speed']
	print(winds)
def pressure():
	pressures=data.json()['list'][0]['main']['pressure']

while True:
	print("Press 1 , Get Temparature")
	print("Press 2 , Get Wind Speed")
	print("Press 3 , Get Pressure")
	print("Press 0 , Exit")
	choice=int(input('Enter your choice: '))
	date_components = input('Enter a date formatted as YYYY-MM-DD: ')
	date_component.append(date_components)
	if choice==1:
		temp()
	elif choice==2:
		wind()
	elif choice==3:
		pressure()
	elif choice==0:
		print('Thank you')
		quit()
	else:
		continue