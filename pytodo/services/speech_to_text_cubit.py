import speech_recognition as sr

r = sr.Recognizer()

# Use the default microphone as the audio source
# For better accuracy of voice command option
# We use recognize_google() instead of recognize_sphinx()

def voiceCommand() -> str:
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source)
        
        print("Listening... Speak now!")
        audio = r.listen(source)

        try:
            # Recognize speech
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            
            return text
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio or say 'quit' to exit program.")
        except sr.RequestError as e:
            print(f"Could not request results from service; {e}")