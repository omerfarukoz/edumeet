import speech_recognition as sr
import pyttsx3

class Listener:


    # This class is used to listen for voice commands and convert them to text.
    # It uses Google speech to text via the SpeechRecognition library and pyttsx3 library.

    engine = pyttsx3.init()
    recognizer = sr.Recognizer()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_for_command(self):

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)  
            audio = self.recognizer.listen(source)  

            try:
                # Google speech to text
                speech_text = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {speech_text}")
                
                if "hey gemini" in speech_text:
                    self.speak("Hello, how can I help you?")
                    
                    command = speech_text.split("hey gemini", 1)[1].strip()
                    # command kullanılarak gemini çağrsı yapılacak
                    print(f"Command received: {command}")
                    return command
            except sr.UnknownValueError:
                print("Could not understand the audio")
            except sr.RequestError as e:
                print(f"Error with the recognition service: {e}")
