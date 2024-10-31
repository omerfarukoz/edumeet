import pygame

class Speaker:

    def __init__(self):
       
        pygame.mixer.init()

    def speak(self, file_path):
        
        pygame.mixer.music.load(file_path)

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


if __name__ == "__main__":
    speaker = Speaker()
    speaker.speak("output.mp3")
