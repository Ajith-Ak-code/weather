import requests
import json
import sys

data=requests.get('https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22')

date_component=''
date_components = input('Enter a date formatted as YYYY-MM-DD: ')
date_component=date_component+date_components

date_input=[]
temp=[]
wind=[]
press=[]

for i in range(sys.maxsize):
	dat,tym=data.json()['list'][i]['dt_txt'].split(' ')
	if dat==date_component:
		temps=data.json()['list'][i]['main']['temp']
		temp.append(temps)
		winds=data.json()['list'][i]['wind']['speed']
		wind.append(winds)
		pressure=data.json()['list'][i]['main']['pressure']
		press.append(pressure)
		break
	elif dat not in date_input:
		date_input.append(dat)

	
while True:
	print("Press 1 , Get Temp")
	print("Press 2 , Get Wind Speed")
	print("Press 3 , Get Pressure")
	print("Press 0 , Exit")
	choice=int(input('Enter your choice: '))
	if choice==1:
		print('Temp: ',temp)
	elif choice==2:
		print('wind: ',wind)
	elif choice==3:
		print('pressure: ',press)
	elif choice==0:
		print('Thank you')
		quit()
	else:
		continue
