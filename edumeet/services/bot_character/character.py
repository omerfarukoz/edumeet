import cv2

class CharacterPlayer:

    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.playing = True
        self.frame = None
        self.current_frame_number = 0  

    def play(self):
        while True:
            if self.playing:
                ret, self.frame = self.cap.read()
                self.current_frame_number += 1 
                if not ret:
                    self.stop()  
                    continue

                cv2.imshow('Video', self.frame)
            else:
                if self.frame is not None:
                    cv2.imshow('Video', self.frame)

            key = cv2.waitKey(30) & 0xFF

            if key == ord('q'):
                self.quit()
                break
            elif key == ord('s'):
                self.stop()  # Stop and reset to first frame
            elif key == ord('r'):
                self.start()

    def start(self):
        self.playing = True

    def stop(self):
        self.playing = False
        # Set frame to first frame (0th position)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 8)
        self.current_frame_number = 0  # Reset frame number
        
        # Display the first frame after stopping
        ret, self.frame = self.cap.read()
        if ret:
            cv2.imshow('Video', self.frame)

    def quit(self):
        self.cap.release()
        cv2.destroyAllWindows()
