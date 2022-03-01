#!/usr/bin/env python3

import speech_recognition as sr
import subprocess
import os
def speech_to_text(path_audio):
	if 'mp3' in path_audio:
		output = path_audio.replace('mp3', 'wav')
		if os.path.isfile(path_audio.replace('mp3', 'wav')) is False:
			command = 'ffmpeg -i'
			input = path_audio
			subprocess.run('{} {} -ar 16k {}'.format(command, input, output), shell=True)
		path_audio = output
	recognizer = sr.Recognizer()	
	with sr.AudioFile(path_audio) as source:
		recorded_audio = recognizer.listen(source)
		print("Done recording")
	try:
		print("Recognizing the text")
		text = recognizer.recognize_google(
				recorded_audio, 
				language="vi-VN"
			)
		print("Decoded Text : {}".format(text))
	except Exception as ex:
		print(ex)
		
path = '/Users/abc/Documents/test'
os.chdir(path)
for file in os.listdir():
	if '.wav' in file:
		speech_to_text(file)
	return_code = subprocess.call(["afplay", file])