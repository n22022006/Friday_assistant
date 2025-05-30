import speech_recognition as sr # Speech recognition library
import pyttsx3 # Text-to-speech engine
import myweb_action 
import pywhatkit # this import is used in playing songs on YouTube, if needed


# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set your assistant's name
WAKE_WORD = "friday"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("Sorry, the service is unavailable right now.")
            return ""

def respond_to_command(command):
    # Customize this part to add more responses
    if "open" in command:
        myweb_action.open_browser(command) 
    elif "play" in command:
        # Assuming you want to play a song on YouTube
         song_name = command.replace("play", "").strip()  # Extract song name from command
         speak(f"Playing {song_name} on YouTube")
         pywhatkit.playonyt(song_name)
        
    elif "introduce" in command :
        speak("I am FRIDAY, a personal assistant created by MR NETIK GOSWAMI . I can help you with various tasks like opening websites, telling the time, and more.")
    elif   command =="hello" or command == "hi":
        speak("HELLO! SIR")
    elif "time" in command:
        # from datetime import datetime
        # current_time = datetime.now().strftime("%H:%M")
        # speak(f"The time is {current_time}")
       from datetime import datetime
       import pytz
       ist = pytz.timezone('Asia/Kolkata')
       now_ist = datetime.now(ist)
       current_time_ist = now_ist.strftime('%H %M %S')
       speak(f"Current time in India (IST):{current_time_ist}")
       print(f"Current time in India (IST):{current_time_ist}")
    elif "exit" in command or "bye" in command:
        speak("ok sir !! Goodbye!")
        exit()
    else:
        # speak("Sorry, I didn't understand that.")
        speak("VOICE IS NOT AUDIBLE , SIR")
# Main loop
speak("  FRIDAY ACTIVATED .....")
while True:
    command = listen()
    if WAKE_WORD in command:
        speak("Yes SIR...")
        command = listen()
        respond_to_command(command)
