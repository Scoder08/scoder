# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
from tkinter import *
import requests
import json
import socket
import time
import pygame
pygame.init()
root=Tk()
root.title("Loading")
root.iconbitmap('icon/weather.ico')
frames = [(PhotoImage(file='images/image.gif',format = 'gif -index '+ str(i)) )for i in range(31)]
def update(ind):

    frame = frames[ind]
    ind += 1
    label.configure(image=frame)
    root.after(31, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
root.after(1000,lambda:root.destroy())
root.mainloop()




def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False
root=Tk()
root.title("Weather")
root.iconbitmap('icon/weather.ico')




if is_connected()==False:
	Label(root,text="Check your Internet Connection!!",fg="Red",relief="solid",cursor="x_cursor").grid(row=3,column=0,columnspan=2,padx=15,pady=10)
	pygame.mixer.music.load("images/sorry.wav")
	pygame.mixer.music.play()

# Enter your API key here 
api_key = "677f3a393bd163dce7f3daf4802157f1"

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
if is_connected()==True:
	city_name = Label(root,text="City Name")
	city_name.grid(row=0,column=0,pady=10)
	global city
	city=Entry(root,width=25)
	city.grid(row=0,column=1,padx=10,pady=10)
# complete_url variable to store 
# complete url address
	global complete_url
	complete_url = base_url + "appid=" + api_key + "&q=" + city.get()


# get method of requests module 
# return response object
global Countries
Countries = {
	'AF': 'AFGHANISTAN',
	'AX': 'ÅLAND ISLANDS',
	'AL': 'ALBANIA',
	'DZ': 'ALGERIA',
	'AS': 'AMERICAN SAMOA',
	'AD': 'ANDORRA',
	'AO': 'ANGOLA',
	'AI': 'ANGUILLA',
	'AQ': 'ANTARCTICA',
	'AG': 'ANTIGUA AND BARBUDA',
	'AR': 'ARGENTINA',
	'AM': 'ARMENIA',
	'AW': 'ARUBA',
	'AU': 'AUSTRALIA',
	'AT': 'AUSTRIA',
	'AZ': 'AZERBAIJAN',
	'BS': 'BAHAMAS',
	'BH': 'BAHRAIN',
	'BD': 'BANGLADESH',
	'BB': 'BARBADOS',
	'BY': 'BELARUS',
	'BE': 'BELGIUM',
	'BZ': 'BELIZE',
	'BJ': 'BENIN',
	'BM': 'BERMUDA',
	'BT': 'BHUTAN',
	'BO': 'BOLIVIA, PLURINATIONAL STATE OF',
	'BQ': 'BONAIRE, SINT EUSTATIUS AND SABA',
	'BA': 'BOSNIA AND HERZEGOVINA',
	'BW': 'BOTSWANA',
	'BV': 'BOUVET ISLAND',
	'BR': 'BRAZIL',
	'IO': 'BRITISH INDIAN OCEAN TERRITORY',
	'BN': 'BRUNEI DARUSSALAM',
	'BG': 'BULGARIA',
	'BF': 'BURKINA FASO',
	'BI': 'BURUNDI',
	'KH': 'CAMBODIA',
	'CM': 'CAMEROON',
	'CA': 'CANADA',
	'CV': 'CAPE VERDE',
	'KY': 'CAYMAN ISLANDS',
	'CF': 'CENTRAL AFRICAN REPUBLIC',
	'TD': 'CHAD',
	'CL': 'CHILE',
	'CN': 'CHINA',
	'CX': 'CHRISTMAS ISLAND',
	'CC': 'COCOS (KEELING) ISLANDS',
	'CO': 'COLOMBIA',
	'KM': 'COMOROS',
	'CG': 'CONGO',
	'CD': 'CONGO, THE DEMOCRATIC REPUBLIC OF THE',
	'CK': 'COOK ISLANDS',
	'CR': 'COSTA RICA',
	'CI': 'CÔTE D\'IVOIRE',
	'HR': 'CROATIA',
	'CU': 'CUBA',
	'CW': 'CURAÇAO',
	'CY': 'CYPRUS',
	'CZ': 'CZECH REPUBLIC',
	'DK': 'DENMARK',
	'DJ': 'DJIBOUTI',
	'DM': 'DOMINICA',
	'DO': 'DOMINICAN REPUBLIC',
	'EC': 'ECUADOR',
	'EG': 'EGYPT',
	'SV': 'EL SALVADOR',
	'GQ': 'EQUATORIAL GUINEA',
	'ER': 'ERITREA',
	'EE': 'ESTONIA',
	'ET': 'ETHIOPIA',
	'FK': 'FALKLAND ISLANDS (MALVINAS)',
	'FO': 'FAROE ISLANDS',
	'FJ': 'FIJI',
	'FI': 'FINLAND',
	'FR': 'FRANCE',
	'GF': 'FRENCH GUIANA',
	'PF': 'FRENCH POLYNESIA',
	'TF': 'FRENCH SOUTHERN TERRITORIES',
	'GA': 'GABON',
	'GM': 'GAMBIA',
	'GE': 'GEORGIA',
	'DE': 'GERMANY',
	'GH': 'GHANA',
	'GI': 'GIBRALTAR',
	'GR': 'GREECE',
	'GL': 'GREENLAND',
	'GD': 'GRENADA',
	'GP': 'GUADELOUPE',
	'GU': 'GUAM',
	'GT': 'GUATEMALA',
	'GG': 'GUERNSEY',
	'GN': 'GUINEA',
	'GW': 'GUINEA-BISSAU',
	'GY': 'GUYANA',
	'HT': 'HAITI',
	'HM': 'HEARD ISLAND AND MCDONALD ISLANDS',
	'VA': 'HOLY SEE (VATICAN CITY STATE)',
	'HN': 'HONDURAS',
	'HK': 'HONG KONG',
	'HU': 'HUNGARY',
	'IS': 'ICELAND',
	'IN': 'INDIA',
	'ID': 'INDONESIA',
	'IR': 'IRAN, ISLAMIC REPUBLIC OF',
	'IQ': 'IRAQ',
	'IE': 'IRELAND',
	'IM': 'ISLE OF MAN',
	'IL': 'ISRAEL',
	'IT': 'ITALY',
	'JM': 'JAMAICA',
	'JP': 'JAPAN',
	'JE': 'JERSEY',
	'JO': 'JORDAN',
	'KZ': 'KAZAKHSTAN',
	'KE': 'KENYA',
	'KI': 'KIRIBATI',
	'KP': 'KOREA, DEMOCRATIC PEOPLE\'S REPUBLIC OF',
	'KR': 'KOREA, REPUBLIC OF',
	'KW': 'KUWAIT',
	'KG': 'KYRGYZSTAN',
	'LA': 'LAO PEOPLE\'S DEMOCRATIC REPUBLIC',
	'LV': 'LATVIA',
	'LB': 'LEBANON',
	'LS': 'LESOTHO',
	'LR': 'LIBERIA',
	'LY': 'LIBYAN ARAB JAMAHIRIYA',
	'LI': 'LIECHTENSTEIN',
	'LT': 'LITHUANIA',
	'LU': 'LUXEMBOURG',
	'MO': 'MACAO',
	'MK': 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF',
	'MG': 'MADAGASCAR',
	'MW': 'MALAWI',
	'MY': 'MALAYSIA',
	'MV': 'MALDIVES',
	'ML': 'MALI',
	'MT': 'MALTA',
	'MH': 'MARSHALL ISLANDS',
	'MQ': 'MARTINIQUE',
	'MR': 'MAURITANIA',
	'MU': 'MAURITIUS',
	'YT': 'MAYOTTE',
	'MX': 'MEXICO',
	'FM': 'MICRONESIA, FEDERATED STATES OF',
	'MD': 'MOLDOVA, REPUBLIC OF',
	'MC': 'MONACO',
	'MN': 'MONGOLIA',
	'ME': 'MONTENEGRO',
	'MS': 'MONTSERRAT',
	'MA': 'MOROCCO',
	'MZ': 'MOZAMBIQUE',
	'MM': 'MYANMAR',
	'NA': 'NAMIBIA',
	'NR': 'NAURU',
	'NP': 'NEPAL',
	'NL': 'NETHERLANDS',
	'NC': 'NEW CALEDONIA',
	'NZ': 'NEW ZEALAND',
	'NI': 'NICARAGUA',
	'NE': 'NIGER',
	'NG': 'NIGERIA',
	'NU': 'NIUE',
	'NF': 'NORFOLK ISLAND',
	'MP': 'NORTHERN MARIANA ISLANDS',
	'NO': 'NORWAY',
	'OM': 'OMAN',
	'PK': 'PAKISTAN',
	'PW': 'PALAU',
	'PS': 'PALESTINIAN TERRITORY, OCCUPIED',
	'PA': 'PANAMA',
	'PG': 'PAPUA NEW GUINEA',
	'PY': 'PARAGUAY',
	'PE': 'PERU',
	'PH': 'PHILIPPINES',
	'PN': 'PITCAIRN',
	'PL': 'POLAND',
	'PT': 'PORTUGAL',
	'PR': 'PUERTO RICO',
	'QA': 'QATAR',
	'RE': 'RÉUNION',
	'RO': 'ROMANIA',
	'RU': 'RUSSIAN FEDERATION',
	'RW': 'RWANDA',
	'BL': 'SAINT BARTHÉLEMY',
	'SH': 'SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA',
	'KN': 'SAINT KITTS AND NEVIS',
	'LC': 'SAINT LUCIA',
	'MF': 'SAINT MARTIN (FRENCH PART)',
	'PM': 'SAINT PIERRE AND MIQUELON',
	'VC': 'SAINT VINCENT AND THE GRENADINES',
	'WS': 'SAMOA',
	'SM': 'SAN MARINO',
	'ST': 'SAO TOME AND PRINCIPE',
	'SA': 'SAUDI ARABIA',
	'SN': 'SENEGAL',
	'RS': 'SERBIA',
	'SC': 'SEYCHELLES',
	'SL': 'SIERRA LEONE',
	'SG': 'SINGAPORE',
	'SX': 'SINT MAARTEN (DUTCH PART)',
	'SK': 'SLOVAKIA',
	'SI': 'SLOVENIA',
	'SB': 'SOLOMON ISLANDS',
	'SO': 'SOMALIA',
	'ZA': 'SOUTH AFRICA',
	'GS': 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS',
	'SS': 'SOUTH SUDAN',
	'ES': 'SPAIN',
	'LK': 'SRI LANKA',
	'SD': 'SUDAN',
	'SR': 'SURINAME',
	'SJ': 'SVALBARD AND JAN MAYEN',
	'SZ': 'SWAZILAND',
	'SE': 'SWEDEN',
	'CH': 'SWITZERLAND',
	'SY': 'SYRIAN ARAB REPUBLIC',
	'TW': 'TAIWAN, PROVINCE OF CHINA',
	'TJ': 'TAJIKISTAN',
	'TZ': 'TANZANIA, UNITED REPUBLIC OF',
	'TH': 'THAILAND',
	'TL': 'TIMOR-LESTE',
	'TG': 'TOGO',
	'TK': 'TOKELAU',
	'TO': 'TONGA',
	'TT': 'TRINIDAD AND TOBAGO',
	'TN': 'TUNISIA',
	'TR': 'TURKEY',
	'TM': 'TURKMENISTAN',
	'TC': 'TURKS AND CAICOS ISLANDS',
	'TV': 'TUVALU',
	'UG': 'UGANDA',
	'UA': 'UKRAINE',
	'AE': 'UNITED ARAB EMIRATES',
	'GB': 'UNITED KINGDOM',
	'US': 'UNITED STATES',
	'UM': 'UNITED STATES MINOR OUTLYING ISLANDS',
	'UY': 'URUGUAY',
	'UZ': 'UZBEKISTAN',
	'VU': 'VANUATU',
	'VE': 'VENEZUELA, BOLIVARIAN REPUBLIC OF',
	'VN': 'VIET NAM',
	'VG': 'VIRGIN ISLANDS, BRITISH',
	'VI': 'VIRGIN ISLANDS, U.S.',
	'WF': 'WALLIS AND FUTUNA',
	'EH': 'WESTERN SAHARA',
	'YE': 'YEMEN',
	'ZM': 'ZAMBIA',
	'ZW': 'ZIMBABWE',
}
def a():
	return weather(complete_url)
def weather(a):
	pygame.mixer.music.load("images/wait.wav")
	pygame.mixer.music.play()
	url=complete_url+city.get()
	v=city.get()
	city.delete(0,END)
	response = requests.get(url) 

# json method of response object 
# convert json format data into 
# python format data 
	x = response.json() 

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
	if x["cod"] != "404":
		y=x['main']
		z=x["sys"]
		w=x["weather"][0]
		ic=w["icon"]
		if ic[2]=='n':
			root.iconbitmap('icon/night.ico')
			tym="Night"
		elif ic[2]=='d':
			root.iconbitmap('icon/day.ico')
			tym="Day"


		print(z)
		code=z["country"]
		country=Countries[code]
		

	# store the value corresponding 
	# to the "temp" key of y 
		current_temperature = y["temp"] 

	# store the value corresponding 
	# to the "pressure" key of y 
		current_pressure = y["pressure"] 

	# store the value corresponding 
	# to the "humidity" key of y 
		current_humidiy = y["humidity"] 

	# store the value of "weather" 
	# key in variable z 
		z = x["weather"]

	# store the value corresponding 
	# to the "description" key at 
	# the 0th index of z 
		weather_description = z[0]["description"]

	# print following values 
		global l
		l=Label(root,text="City :"+v.upper()+" ("+country+")"+"\nTemperature = " +str(int(current_temperature-273.16)) +"°C"+"\nTime = "+tym+"\n Atmospheric pressure (in hPa unit) = " +str(current_pressure) +"\n Humidity (in percentage) = " +str(current_humidiy) +"\n Description = " +str(weather_description),relief="solid")
		l.grid(row=2,column=0,columnspan=2,pady=5)


	else:
		p=Label(root,text=" City Not Found ",fg="red")
		p.config(width=32,height=6)
		p.grid(row=2,column=0,columnspan=2,pady=5)
		pygame.mixer.music.load("images/can,t find.wav")
		pygame.mixer.music.play()



	# store the value of "main" 
	# key in variable y 
if is_connected()==True:
	sub=Button(root,text="Submit",command=weather,cursor="hand2")
	sub.grid(row=1,column=0,columnspan=2)
	root.bind('<Return>',weather)
root.mainloop()