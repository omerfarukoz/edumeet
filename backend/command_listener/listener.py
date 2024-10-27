import speech_recognition as sr
import pyttsx3
class Listener:

    engine = pyttsx3.init()

    recognizer = sr.Recognizer()

    def speak(self,text):
      
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_for_hello(self,):
       
        with sr.Microphone() as source:
            
            self.recognizer.adjust_for_ambient_noise(source)  
            audio = self.recognizer.listen(source)  

            try:
                # Google speech to text
                speech_text = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {speech_text}")
                
                
                if "hey gemini" in speech_text:
                    self.speak("Hello, how can I help you?")
            except sr.UnknownValueError:
                print("Could not understand the audio")
            except sr.RequestError as e:
                print(f"Error with the recognition service: {e}")



    def get_hundred_word(self):
        word_count = 0
        while True:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source)

                audio = self.recognizer.listen(source)

                try:
                    speech_text = self.recognizer.recognize_google(audio).lower()
                    word_count += speech_text.count(" ") + 1  # Include the first word
                    if word_count >= 100:
                        print(f"You said: {speech_text}")
                        word_count = 0  # Reset word count
                except sr.RequestError as e:
                     print(f"Error with the recognition service: {e}")   



if __name__ == "__main__":
    listener = Listener()
   
    while True:

        listener.get_hundred_word()


