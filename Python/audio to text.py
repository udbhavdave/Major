# import speech_recognition as sr
# import sys
#
# # read filename from arguments
# filename = ("C:\\Users\\utkar\\Downloads\\crowd.mp3")
#
# # initialize the recognizer
# r = sr.Recognizer()
#
# # open the file
# with sr.AudioFile(filename) as source:
#     # listen for the data (load audio to memory)
#     audio_data = r.record(source)
#     # recognize (convert from speech to text)
#     text = r.recognize_google(audio_data)
#     print(text)

#Python 2.x program to transcribe an Audio file
import speech_recognition as sr
import connection

AUDIO_FILE = ("..\\audio\\Welcome.wav")

# use the audio file as the audio source

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
	#reads the audio file. Here we use record instead of
	#listen
	audio = r.record(source)

try:
	print("The audio file contains: " + r.recognize_google(audio))
	connection.insertAudio(2, r.recognize_google(audio), AUDIO_FILE)

except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")

# except sr.RequestError as e:
# 	print("Could not request results from Google Speech
# 			Recognition service; {0}".format(e))
