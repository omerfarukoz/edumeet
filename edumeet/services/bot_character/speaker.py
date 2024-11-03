import pygame

class Speaker:

    # This class is used to play google text-to-speech audio files.
    
    def __init__(self):
       
        pygame.mixer.init()

    def speak(self, file_path):
        
        pygame.mixer.music.load(file_path)

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
