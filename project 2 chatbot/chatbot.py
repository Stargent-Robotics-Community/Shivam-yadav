from playsound import playsound
from datetime import datetime
import os
import pyttsx3
import speech_recognition as sr
i=1
while(i==1):
  r=sr.Recognizer()
  with sr.Microphone() as source:
     r.adjust_for_ambient_noise(source)
     r.pause_threshold=1
     print("speak now")
     audio=r.listen(source)
  try:
    text=r.recognize_google(audio)

    print(text)
  except:
      print("sorry speak again ")
  s=pyttsx3.init()
  v=s.getProperty('voices')
  v
  s.setProperty('voice',v[1].id)

  try:
      if text=="hello":
         print(": hello, how may i help you?")
         s.say("hello, how may i help you?")
         s.runAndWait()

      elif text=="who are you":
         print(": i am a chat bot. I will try to answer questions.\n"
             "sometimes I need help as I am in develping stage.\n So How may I help you today")
         s.say("I am a chat bot. I will try to answer questions. Sometimes I need help as I am in develping stage. So How may I help you today")
         s.runAndWait()
      elif text=="hey":
         print(": hey!!")
         s.say("hey!")
         s.runAndWait()

      elif text=="play song":
         print(": playing a song")
         playsound('E:\\1.mp3')
      elif text=="tell joke":
         print(": what did one plate say to his friend? Tonight, dinner's on me!")
         s.say("what did one plate say to his friend? Tonight, dinner's on me!")
         s.runAndWait()
      elif text==("do you love me"):
         print(": ofcourse, I love you baby")
         s.say("ofcourse, I love you baby")
         s.runAndWait()
      elif text=="good morning":
         print(": good morning dear")
         s.say("good morning dear")
         s.runAndWait()
      elif text=="good evening":
         print(": good evening dear")
         s.say("good evening dear")
         s.runAndWait()
      elif text=="who is the Prime Minister of India":
         print(": Prime Minister of India is Mr. Narendra Modi")
         s.say("Prime Minister of India is Mr. Narendra Modi")
         s.runAndWait()
      elif text=="who is the Chief Minister of Rajasthan":
         print(": Chief Minister of Rajasthan is Ashok Gehloet")
         s.say("Chief Minister of Rajasthan is Ashok Gehloet")
         s.runAndWait()
      elif text=="who made this program":
         print(": This program is made by Master Shivam Yadav")
         s.say("This program is made by Master Shivam Yadav")
         s.runAndWait()
      elif text=="tell me date and time":
         print(datetime.now())
         s.say(datetime.now())
         s.runAndWait()
      elif text=="open Chrome":
         print(": opening chrome")
         s.say("opening chrome")
         os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
      elif text=="what is your name":
          print(": I am shy version 1.0.0.1")
          s.say("I am shy version 1.0.0.1")
          s.runAndWait()
      elif text=="suggest me movies":
          print("you can watch Interstellar. It is a epic science fiction film")
          s.say("you can watch Interstellar. It is a epic science fiction film")
          s.runAndWait()
      elif text=="suggest me tv series":
          print("you can watch breaking bad. It is an American neo-Western crime drama. ")
          s.say("you can watch breaking bad. It is an American neo-Western crime drama. ")
          s.runAndWait()
  except:
      print(": sorry try again")
      s.say("sorry, Try again")
  i=int(input("enter 0 for stop and 1 to continue:"))

print("thanks for using")







