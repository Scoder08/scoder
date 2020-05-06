from tkinter import *
import pyttsx3
root1=Tk()
root1.title("Projects")
roots=LabelFrame(root1,padx=20,pady=20)
roots.pack(padx=10,pady=10)
def speak(a,text):
		converter = pyttsx3.init() 
	  
	# Set properties before adding 
	# Things to say 
	  
	# Sets speed percent  
	# Can be more than 100 
		converter.setProperty('rate', 150) 
	# Set volume 0-1 
		converter.setProperty('volume', 0.7)
		converter.setProperty('voice', "Female") 
	  
	# Queue the entered text  
	# There will be a pause between 
	# each one like a pause in  
	# a sentence 
		converter.say(text) 

	  
	# Empties the say() queue 
	# Program will not continue 
	# until all speech is done talking 
		converter.runAndWait()
def w():
	root1.destroy()
	import requests
	import json
	import socket
	import time
	import pygame
	global ss
	from webbrowser import open
	import pyttsx3
	import os 

	ss=None
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



	#####



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

	def speak(a,text):
		converter = pyttsx3.init() 
	  
	# Set properties before adding 
	# Things to say 
	  
	# Sets speed percent  
	# Can be more than 100 
		converter.setProperty('rate', 160) 
	# Set volume 0-1 
		converter.setProperty('volume', 1) 
	  
	# Queue the entered text  
	# There will be a pause between 
	# each one like a pause in  
	# a sentence 
		converter.say(text) 

	  
	# Empties the say() queue 
	# Program will not continue 
	# until all speech is done talking 
		converter.runAndWait() 



	if is_connected()==False:
		Label(root,text="Check your Internet Connection!!",fg="Red",relief="solid",cursor="x_cursor").grid(row=3,column=0,columnspan=2,padx=15,pady=10)
		canvas=Canvas(root,width=15,height=15,bg="white")
		canvas.create_oval(1,1,12,12, fill='red')
		speak(0,"Bro! Check  your internet connection")

		canvas.grid(row=1,column=1,sticky="E")

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
		if len(city.get())==3:
			city.insert(3,"-")
		speak(0,"Welcome to! Weather")
	# complete_url variable to store 
	# complete url address
		global complete_url
		complete_url = base_url + "appid=" + api_key + "&q=" + city.get()
		canvas=Canvas(root,width=18,height=18,bg="white")
		canvas.create_oval(3,3,15,15, fill='green')
		canvas.grid(row=1,column=1,sticky="E")


	global Countries
	Countries = {
	'AF': 'AFGHANISTAN',
	'AX': 'ÅLAND ISLANDS',
	'AL': 'ALBANIA','DZ': 'ALGERIA','AS': 'AMERICAN SAMOA','AD': 'ANDORRA',
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
	'BI': 'BURUNDI','KH': 'CAMBODIA','CM': 'CAMEROON','CA': 'CANADA','CV': 'CAPE VERDE','KY': 'CAYMAN ISLANDS','CF': 'CENTRAL AFRICAN REPUBLIC','TD': 'CHAD','CL': 'CHILE','CN': 'CHINA','CX': 'CHRISTMAS ISLAND','CC': 'COCOS (KEELING) ISLANDS','CO': 'COLOMBIA','KM': 'COMOROS','CG': 'CONGO','CD': 'CONGO, THE DEMOCRATIC REPUBLIC OF THE','CK': 'COOK ISLANDS','CR': 'COSTA RICA','CI': 'CÔTE D\'IVOIRE','HR': 'CROATIA','CU': 'CUBA','CW': 'CURAÇAO','CY': 'CYPRUS','CZ': 'CZECH REPUBLIC','DK': 'DENMARK','DJ': 'DJIBOUTI','DM': 'DOMINICA','DO': 'DOMINICAN REPUBLIC','EC': 'ECUADOR','EG': 'EGYPT','SV': 'EL SALVADOR','GQ': 'EQUATORIAL GUINEA','ER': 'ERITREA','EE': 'ESTONIA','ET': 'ETHIOPIA','FK': 'FALKLAND ISLANDS (MALVINAS)','FO': 'FAROE ISLANDS','FJ': 'FIJI','FI': 'FINLAND','FR': 'FRANCE','GF': 'FRENCH GUIANA','PF': 'FRENCH POLYNESIA','TF': 'FRENCH SOUTHERN TERRITORIES','GA': 'GABON',
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
	'US': "USA",
	'TM': 'TURKMENISTAN','TC': 'TURKS AND CAICOS ISLANDS',
	'TV': 'TUVALU','UG': 'UGANDA','UA': 'UKRAINE','GB': 'UNITED KINGDOM','UM': 'UNITED STATES MINOR OUTLYING ISLANDS','UY': 'URUGUAY','UZ': 'UZBEKISTAN','VU': 'VANUATU','VE': 'VENEZUELA, BOLIVARIAN REPUBLIC OF','VN': 'VIET NAM','VG': 'VIRGIN ISLANDS, BRITISH','VI': 'VIRGIN ISLANDS, U.S.','WF': 'WALLIS AND FUTUNA','EH': 'WESTERN SAHARA','YE': 'YEMEN','ZM': 'ZAMBIA','ZW': 'ZIMBABWE',
	}

	def weather(a):
		if is_connected()==False:
			canvas=Canvas(root,width=18,height=18,bg="white")
			canvas.create_oval(3,3,15,15, fill='red')
			canvas.grid(row=1,column=1,sticky="E")
			ss=Label(root,text="Check your Internet Connection!!",fg="Red",cursor="x_cursor")
			ss.config(width=32,height=7)
			ss.grid(row=2,column=0,columnspan=2,pady=10)
			speak(0,"Bro! Check your internet connection")
		else:
			###
			canvas=Canvas(root,width=18,height=18,bg="white")
			canvas.create_oval(3,3,15,15, fill='green')
			canvas.grid(row=1,column=1,sticky="E")

			pygame.mixer.music.load("images/click.mp3")
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


			country=""
			if "country" in z:
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
			temp=int(current_temperature-273.16)
			language='en'

		# print following values 
			global l
			l=Label(root,text="City :"+v.upper()+" ("+country+")"+"\nTemperature = " +str(int(current_temperature-273.16)) +"°C"+"\nTime = "+tym+"\n Atmospheric pressure (in hPa unit) = " +str(current_pressure) +"\n Humidity (in percentage) = " +str(current_humidiy) +"\n Description = " +str(weather_description),relief="solid")
			l.grid(row=2,column=0,columnspan=2,pady=5)
			if current_temperature-273.16>=0:
				speak(0,"Temperature in "+v+"! is "+str(int(current_temperature-273.16))+"degree celcius") 
			else:
				speak(0,"minus"+str(int(current_temperature-273.16))+"degree celcius") 




		else:
			p=Label(root,text=" City Not Found ",fg="red")
			speak(0,"Sorry Brooo!! City not found")
			p.config(width=32,height=6)
			p.grid(row=2,column=0,columnspan=2,pady=5)



		# store the value of "main" 
		# key in variable y 
	if is_connected()==True:
		sub=Button(root,text="Submit",command=lambda:weather(0),cursor="hand2")
		sub.grid(row=1,column=0,columnspan=2)
		root.bind('<Return>',weather)
	root.mainloop()

def o():
	import cv2
	from tkinter import filedialog
	from PIL import ImageTk,Image
	import time
	from time import sleep
	import requests
	import pygame
	import pyttsx3
	pygame.init()
	key = cv2. waitKey(1)
	webcam = cv2.VideoCapture(0)
	sleep(2)
	root=Tk()
	root.title("Text")
	root.iconbitmap('icon/eyeverse.ico')
	def ocr_space_file(filename, overlay=False, api_key='b3026ffa6488957', language='en'):
	    """ OCR.space API request with local file.
	        Python3.5 - not tested on 2.7
	    :param filename: Your file path & name.
	    :param overlay: Is OCR.space overlay required in your response.
	                    Defaults to False.
	    :param api_key: OCR.space API key.
	                    Defaults to 'helloworld'.
	    :param language: Language code to be used in OCR.
	                    List of available language codes can be found on https://ocr.space/OCRAPI
	                    Defaults to 'en'.
	    :return: Result in JSON format.
	    """

	    payload = {'isOverlayRequired': overlay,
	               'apikey': api_key,
	               'language': language,
	               }
	    with open(filename, 'rb') as f:
	        r = requests.post('https://api.ocr.space/parse/image',
	                          files={filename: f},
	                          data=payload,
	                          )
	    return r.json()

	def speak(a,text):
		converter = pyttsx3.init() 
	  
	# Set properties before adding 
	# Things to say 
	  
	# Sets speed percent  
	# Can be more than 100 
		converter.setProperty('rate', 150) 
	# Set volume 0-1 
		converter.setProperty('volume', 0.7) 
	  
	# Queue the entered text  
	# There will be a pause between 
	# each one like a pause in  
	# a sentence 
		converter.say(text) 

	  
	# Empties the say() queue 
	# Program will not continue 
	# until all speech is done talking 
		converter.runAndWait() 
	speak(0,"Welcome to Eyeverse")
	# Use examples:
	def cap():
		while True:
			try:
				check, frame = webcam.read()
				print(check) #prints true as long as the webcam is running
				print(frame) #prints matrix values of each framecd 
				cv2.imshow("Capturing", frame)
				key = cv2.waitKey(1)
				if key == ord('s'):
					pygame.mixer.music.load("images/click.mp3")
					pygame.mixer.music.play()
					cv2.imwrite(filename='saved_img.jpg', img=frame)
					webcam.release()
					print("Processing image...")
					img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
					print("Converting RGB image to grayscale...")
					gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
					print("Converted RGB image to grayscale...")
					print("Resizing image to 28x28 scale...")
					img_ = cv2.resize(gray,(28,28))
					print("Resized...")
					print("Image saved!")
					test_file = ocr_space_file(filename='saved_img.jpg', language='pol')
					cv2.destroyAllWindows()
					a=test_file["ParsedResults"]
					b=a[0]
					c=b['ParsedText']
					if c=="":
						Label(root,text="Can't find any text!!",fg="Red").pack()
						speak(0,"Sorry, I can't find any text")
					else:
						Label(root,text=c,bg="cyan").pack()
						speak(0,c)

	            
					break
	        
				elif key == ord('q'):
					webcam.release()
					cv2.destroyAllWindows()
					break
			

			except(KeyboardInterrupt):
				print("Turning off camera.")
				webcam.release()
				print("Camera off.")
				print("Program ended.")
				cv2.destroyAllWindows()
				break
	def opens():
		global img
		root.filename=filedialog.askopenfilename(initialdir="/Users/shres/Desktop/gui/images",title="Select a file",filetypes=(("png files","*.png"),("all files","*.*"),("jpg files","*.jpg")))
		img=ImageTk.PhotoImage(Image.open(root.filename))
		test_file = ocr_space_file(filename=root.filename, language='pol')
		a=test_file["ParsedResults"]
		b=a[0]
		c=b['ParsedText']
		if c=="":
			Label(root,text="Can't find any text!!",fg="Red").pack()
			speak(0,"SOrry, I can't find any text")
		else:
			Label(root,text=c,bg="cyan").pack()
			speak(0,c)
		


	btn=Button(root,text="Choose File",command=opens).pack()
	click=Button(root,text="Capture",command=cap).pack()

	root.mainloop()

Label(roots,text="PROJECTS",font="Helvetica 12 bold",fg="green").grid(row=0,column=0,columnspan=2,padx=10,pady=10)
Label(roots,text="WEATHER",font="Helvetica 8 bold",fg="red").grid(row=1,column=0)
Button(roots,text="Tour",command=w,fg="brown").grid(row=1,column=1)
Label(roots,text="EYEVERSE",font="Helvetica 8 bold",fg="red").grid(row=2,column=0)
Button(roots,text="Tour",command=o,fg="brown").grid(row=2,column=1)
speak(0,"Here are! Shresth's Projects")
root1.mainloop()