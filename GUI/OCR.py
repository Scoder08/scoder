import cv2
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import time
from time import sleep
import requests
import pygame
from gtts import gTTS
from tempfile import TemporaryFile
import pyttsx3

def func2():
	pygame.init()
	key = cv2. waitKey(1)
	webcam = cv2.VideoCapture(0)
	sleep(2)
	root=Tk()
	root.title("Text")
	root.iconbitmap('icon/eyeverse.ico')
	def ocr_space_file(filename, overlay=False, api_key='your api key here', language='en'):
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
					Label(root,text=c,bg="cyan").pack()
					Button(root,text="Speak",command=lambda: speak(0,c)).pack()

	            
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
		else:
			Label(root,text=c,bg="cyan").pack()
			Button(root,text="Speak",command=lambda: speak(0,c)).pack()
		


	btn=Button(root,text="Choose File",command=opens).pack()
	click=Button(root,text="Capture",command=cap).pack()

	root.mainloop()
func2()
