from distutils.log import error
from googletrans import Translator
import speech_recognition as spr
import os
from gtts import gTTS
import googletrans
a=googletrans.LANGUAGES
print("select the way to translate \n1.voice \n2.image \n3.text")
n=int(input())
recog1 = spr.Recognizer()
mc = spr.Microphone()
translator = Translator()
print("enter to language to be converted")
from_lang=input()
print("enter the language after conversion")
to_lang=input()
try:
	from_lang=list(a.keys())[list(a.values()).index(from_lang)]
	to_lang=list(a.keys())[list(a.values()).index(to_lang)]
except ValueError as e:
	print("enter correct spellings")
	from_lang=input()
	to_lang=input()
	from_lang=list(a.keys())[list(a.values()).index(from_lang)]
	to_lang=list(a.keys())[list(a.values()).index(to_lang)]

def trans(n):
	sub=True
	print(n)
	if sub==True:
		if n==1:
			print("Speak a sentence...")
			with mc as source:
				recog1.adjust_for_ambient_noise(source, duration=0.2)
				audio = recog1.listen(source)
				get_sentence = recog1.recognize_google(audio)
			try:
				with mc as source:
					recog1.adjust_for_ambient_noise(source, duration=0.2)
					audio = recog1.listen(source)
					get_sentence = recog1.recognize_google(audio)
					print("Phase to be Translated :"+ get_sentence)
					text_to_translate = translator.translate(get_sentence,src= from_lang,dest= to_lang)
					text = text_to_translate.text
					print(text)
					speak = gTTS(text=text, lang=to_lang, slow= False)
					speak.save("captured_voice.mp3")
					os.system("start captured_voice.mp3")
			except spr.UnknownValueError:
				print("Unable to Understand the Input")
			except spr.RequestError as e:
				print("Unable to provide Required Output".format(e))

		elif n==2:
			import cv2
			import pytesseract
			pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
			print("select image and put in translator")
			img='C:\\Users\\malli\\OneDrive\\Desktop\\translator\\'
			inp=input()
			img=img+inp
			img=cv2.imread(img)
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
			rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
			dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
			contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
			im2 = img.copy()
			file = open("recognized.txt", "w+")
			file.write("")
			file.close()
			for cnt in contours:
				x, y, w, h = cv2.boundingRect(cnt)
				rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
				cropped = im2[y:y + h, x:x + w]
				file = open("recognized.txt", "a")
				text = pytesseract.image_to_string(cropped)
				file.write(text)                                                                                       
				file.close()
			file=open('recognized.txt','r')
			text=file.read()
			print(text)
			translator=Translator(service_urls=['translate.googleapis.com'])
			translated_text=translator.translate(text,src=from_lang,dest=to_lang)
			t_text=translated_text.text
			speak = gTTS(text=t_text, lang=to_lang, slow= False)
			print(t_text)
			speak.save("captured_voice.mp3")
			os.system("start captured_voice.mp3")
		elif n==3:
			text=input("enter ur sentence")
			sub1=True
			if sub1:
				translator=Translator(service_urls=['translate.googleapis.com'])
				translated_text=translator.translate(text,src=from_lang,dest=to_lang)
				t_text=translated_text.text
				speak = gTTS(text=t_text, lang=to_lang, slow= False)
				print(t_text)
				speak.save("captured_voice.mp3")
				os.system("start captured_voice.mp3")
trans(n)