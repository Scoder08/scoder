from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyscreenshot as ImageGrab
from PIL import Image 
from os import system


a_no=input("Enter your Lisence no. : ")
Dob=input("Enter date of birth (dd-mm-yyyy): ")
driver = webdriver.Chrome('C:/Users/shres/Desktop/chromedriver.exe')

driver.get("https://parivahan.gov.in/rcdlstatus/?pur_cd=101")
sleep(2)
   # grab fullscreen




li_no= driver.find_element_by_xpath("//input[@name='form_rcdl:tf_dlNO']")
li_no.clear()
li_no.send_keys(a_no)
do= driver.find_element_by_xpath("//input[@name='form_rcdl:tf_dob_input']")
do.clear()
do.send_keys(Dob)
im = ImageGrab.grab()

    # save image file
im.save('screenshot.png')
im = Image.open(r"screenshot.png") 
	  
	# Size of the image in pixels (size of orginal image) 
	# (This is not mandatory) 
width, height = im.size 
	  
	# Setting the points for cropped image 
left = width/4+100
right = 2*left+10
bottom = 3 * height / 4
top=bottom-100
	  
	# Cropped image of above dimension 
	# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 
im1.save('screenshot.png')
def scan():
	global x
	import os
	import io
	from gtts import gTTS
	from google.cloud import vision
	from matplotlib import pyplot as plt
	from matplotlib import patches as pch

	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'firstkey.json'

	client = vision.ImageAnnotatorClient()

	f = "screenshot.png"
	with io.open(f, 'rb') as image:
		content = image.read()

	image = vision.types.Image(content = content)
	response = client.text_detection(image = image)
	texts = response.text_annotations
	a=str(texts[0])
	for i in range(len(a)):
		if a[i]=='d'and a[i+1]=='e':
			b=str(a[i+12:])
			break
	for i in range(len(str(b))):
		if b[i:i+13]=='bounding_poly':
			c=b[:i]
			break
	d=list(c)
	e=2
	for i in range(len(d)):
		if d[i]=="\\":
			x=str(''.join(d[2:i]))
			break
	do= driver.find_element_by_xpath("//input[@name='form_rcdl:j_idt34:CaptchaID']")
	do.clear()
	do.send_keys(x)
	print(x)
	a=driver.find_element_by_xpath("//button[@name='form_rcdl:j_idt46']").click()
	sleep(2)
	try:
		driver.find_element_by_class_name('ui-messages-error-summary')
		do= driver.find_element_by_xpath("//input[@name='form_rcdl:j_idt34:CaptchaID']")
		do.clear()
		im = ImageGrab.grab()

	    # save image file
		im.save('screenshot.png')
		im = Image.open(r"screenshot.png") 
		  
		# Size of the image in pixels (size of orginal image) 
		# (This is not mandatory) 
		width, height = im.size 
		  
		# Setting the points for cropped image 
		left = width/4+100
		right = 2*left+10
		bottom = (4 * height / 5)+50
		top=bottom-100
		  
		# Cropped image of above dimension 
		# (It will not change orginal image) 
		im1 = im.crop((left, top, right, bottom)) 
		im1.save('screenshot.png')
		scan()
	except:
		driver.execute_script("window.scrollTo(0, 350)")
		sleep(1)
		im = ImageGrab.grab()

	    # save image file
		im.save('result.jpg')
		im = Image.open(r"result.jpg") 
		  
		# Size of the image in pixels (size of orginal image) 
		# (This is not mandatory) 
		width, height = im.size 
		  
		# Setting the points for cropped image 
		left = width/100+10
		right = width-400
		bottom = height-50
		top=bottom-780
		  
		# Cropped image of above dimension 
		# (It will not change orginal image) 
		im1 = im.crop((left, top, right, bottom)) 
		im1.save('result.jpg')
		driver.close()
		im = Image.open(r"result.jpg")  
	  
	# This method will show image in any image viewer  
		im.show()
		system('cls')
		print("See result on result.jpg")

    # show image in a window
scan()




