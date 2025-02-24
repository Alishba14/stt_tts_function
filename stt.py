import speech_recognition as sr
from speech_recognition import google
# import pyaudio as py 
# import pyttsx3 as ptts 
# import os



#Initialize the recognizer
rec= sr.Recognizer()    #it interacts with Pc's microphone

#func to recognize and receive audio/speech 
def audio_recognizer():
    #while loop for if there is any error then it will restart the function
    while(True):
        #try and except for the error handling scenario
        try:
        #first way to solve error is: use microphone as the source
            with sr.Microphone(device_index=1) as source: 
            #use the recognizer object 'rec' for recognizing speech and adjusts ambient noises
                rec.adjust_for_ambient_noise(source,duration=0.1)
            #listen through recognizer and save it as audio
                audio=rec.listen(source)
            #use tensorflow recognizer to recognize audio and save it as a text
                Text=rec.recognize_google(audio)
            
                return Text
        except sr.RequestError as e:
            print("Could not request results from the speech recognition service; {0}".format(e))
        except sr.UnknownValueError:
            print("Sorry! Could not understand the audio")
        except ImportError:
            print("Make sure that you have tensorflow installed, otherwise program will crash")
            
        # While loop stop condition
            
def recognized_audio_into_textform(text):
    file=open('audio_text','a')   #if the file is not in the directory then it will create one and the second parameter is used for appending the converted audio text into at the end of that file
    file.write(text)
    file.write("\n") #for new line after each break while speaking
    file.close()  #closing the running file when the task is done
    return

while(True):
    text=audio_recognizer()
    recognized_audio_into_textform(text)
    print("Wrote text")
    
    #while loop stop codition