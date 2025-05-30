import pyttsx3
import webbrowser as net
def open_browser(command):
    engine = pyttsx3.init()
    if command == "open youtube":
        print("Opening YouTube video...")
        engine.say("OPENING YOUTUBE VIDEO")
        engine.runAndWait()
        url = "https://youtu.be/bKDdT_nyP54?si=_Wi-d-eyBEB7v0ij"
        net.open(url)
    elif command == "open whatsapp":
        print("Opening WhatsApp...")
        engine.say("OPENING WHATSAPP")
        engine.runAndWait()
        url = "https://web.whatsapp.com/"
        net.open(url)
    elif command == "open github":
        print("Opening github...")
        engine.say("OPENING GITHUB")  
        engine.runAndWait()  
        url = "https://github.com/"
        net.open(url)
    else:
        print("Command not recognized:", command)

