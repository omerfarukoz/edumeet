from google.cloud import videointelligence
from google.cloud import vision
import io
import asyncio

class GoogleVisionService:

    def __init__(self):
        self.video_client = videointelligence.VideoIntelligenceServiceClient()
        self.image_client = vision.ImageAnnotatorClient()


    async def analyze_video(self, video_path):

        features = [
            videointelligence.Feature.LABEL_DETECTION,
            videointelligence.Feature.TEXT_DETECTION,
            videointelligence.Feature.SPEECH_TRANSCRIPTION,
        ]

        config = videointelligence.SpeechTranscriptionConfig(
        language_code="en-US" )
 


        with open(video_path, "rb") as f:
            video_content = f.read()

        request = videointelligence.AnnotateVideoRequest(
            features=features, input_content=video_content,
            video_context=videointelligence.VideoContext(speech_transcription_config=config)
        )

        operation = self.video_client.annotate_video(request=request)

        try:
            result = operation.result(timeout=120)
            annotation_results = result.annotation_results[0]
            transcript_result = result.annotation_results[1]

            with open("my_file.txt", "w") as file:
                file.write(str(result))

            label_descriptions = []
            for annotation in annotation_results.shot_label_annotations:
                if annotation.entity.description:
                    label_descriptions.append(annotation.entity.description)

            text_annotations = []
            for text_annotation in annotation_results.text_annotations:
                if text_annotation.text:
                    text_annotations.append(text_annotation.text)

            
            speech_transcriptions = []
            for speech_transcription in transcript_result.speech_transcriptions:
                if speech_transcription.alternatives:
                    speech_transcriptions.append(speech_transcription.alternatives[0].transcript)

            data = (label_descriptions, text_annotations, speech_transcriptions)


            print(speech_transcriptions)

            with open("my_file2.txt", "w") as file:

                file.write(str(label_descriptions))
                file.write("\n")
                file.write(str(text_annotations))
                file.write("\n")
                file.write(str(speech_transcriptions))

            return {
                "label_descriptions": label_descriptions,
                "text_annotations": text_annotations,
                "speech_transcriptions": speech_transcriptions
            }
        
        except TimeoutError:
            raise Exception("Timeout Error")
        


    async def detect_face_emotions(self,image_path):
        """Detects faces in an image and extracts emotions.

        Args:
            path: The path to the image file.

        Returns:
            A list of detected faces with their emotions in a dictionary format.
        """

        

        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = self.image_client.face_detection(image=image)
        faces = response.face_annotations

        face_emotions = []
        for face in faces:
            emotions = {
                "joy": face.joy_likelihood,
                "sorrow": face.sorrow_likelihood,
                "anger": face.anger_likelihood,
                "surprise": face.surprise_likelihood,
                "under_exposed": face.under_exposed_likelihood,
                "blurred": face.blurred_likelihood,
                "headwear": face.headwear_likelihood,
            }
            face_emotions.append(emotions)
        print(face_emotions)
        return face_emotions

        

    async def detect_text(self, image_path):
        """Detects text in an image at the given path.

        Args:
            image_path: The path to the image file.

        Returns:
            A list of TextAnnotation objects containing detected text.

        Raises:
            Exception: If an error occurs during image analysis.
        """

        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = self.image_client.text_detection(image=image)
        texts = response.text_annotations

        all_texts = []
        for text in texts:

            all_texts.append(text.description)

        if response.error.message:
            raise Exception(f'Error during text detection: {response.error.message}')
        print(all_texts)
        return all_texts
    
    async def detect_document_all_text(self, path):
        """Detects document features in an image and returns all text as a single string."""
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = self.image_client.document_text_detection(image=image)       
        return response.full_text_annotation.text



    async def detect_labels(self, image_path):
        """Detects labels in an image at the given path.

        Args:
            image_path: The path to the image file.

        Returns:
            A list of LabelAnnotation objects containing detected labels.

        Raises:
            Exception: If an error occurs during image analysis.
        """

        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = self.image_client.label_detection(image=image)
        labels = response.label_annotations

        if response.error.message:
            raise Exception(f'Error during label detection: {response.error.message}')
        all_labels = []
        # Process or return the detected labels
        for label in labels:
            all_labels.append(label.description)

        print(all_labels)
        return all_labels   
    
if __name__ == "__main__":
    api = GoogleVisionService()

  # asyncio.run(api.detect_document_all_text("/Users/celalcanaslan/Desktop/Screenshot 2024-10-27 at 15.19.59.png"))
  # asyncio.run(api.detect_labels("/Users/celalcanaslan/Desktop/Screenshot 2024-10-27 at 15.19.59.png"))
  # asyncio.run(api.detect_text("/Users/celalcanaslan/Desktop/Screenshot 2024-10-27 at 15.19.59.png"))
  # asyncio.run(api.analyze_video("/Users/celalcanaslan/Downloads/last-video.mp4"))
  # asyncio.run(api.detect_face_emotions("/Users/celalcanaslan/Downloads/Angry-Person-Mad-Transparent-PNG.png"))
 