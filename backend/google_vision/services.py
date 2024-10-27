from google.cloud import videointelligence
from google.cloud import vision
import io


class GoogleVisionService:

    def __init__(self):
        self.video_client = videointelligence.VideoIntelligenceServiceClient()
        self.image_client = vision.ImageAnnotatorClient()


class GoogleVisionService:

    def __init__(self):
        self.video_client = videointelligence.VideoIntelligenceServiceClient()
        self.image_client = vision.ImageAnnotatorClient()


    def analyze_camera(self, video_path):
        """Analyzes a video at the given local path for people and emotions.

        Args:
            video_path: The local path to the video file (e.g., "/path/to/your/video.mp4").

        Returns:
            A dictionary containing the number of faces detected, the likelihood name for adult content,
            and a list of emotion likelihoods for each detected face.

        Raises:
            Exception: If an error occurs during video analysis.
        """

        features = [videointelligence.Feature.PERSON_DETECTION, videointelligence.Feature.EMOTION_ANALYSIS]

        # Read the video file into memory
        with open(video_path, "rb") as f:
            video_content = f.read()

        # Create an input video object
        input_video = videointelligence.InputVideo(input_content=video_content)

        # Create a request object
        request = videointelligence.AnnotateVideoRequest(
            input_uri=input_video, features=features
        )

        # Send the request to the Video Intelligence API
        operation = self.video_client.annotate_video(request=request)

        try:
            result = operation.result(timeout=60)  # Set a timeout for video processing
        except TimeoutError:
            raise Exception("Video analysis timed out. Consider longer videos or optimizing requests.")

        # Extract relevant information from the response
        face_count = len(result.annotation_results[0].person_detection_annotations)
        safe_search = result.annotation_results[0].safe_search_detection
        likelihood_name = vision.Likelihood(safe_search.adult).name

        # Extract emotion information
        emotion_likelihoods = []
        for annotation in result.annotation_results[0].emotion_recognition_annotations:
            emotion_likelihoods.append({
                "joy": annotation.joy_likelihood,
                "anger": annotation.anger_likelihood,
                "surprise": annotation.surprise_likelihood,
                "sorrow": annotation.sorrow_likelihood,
                "uncertainty": annotation.uncertainty_likelihood
            })

        return {
            'face_count': face_count,
            'likelihood_name': likelihood_name,
            'emotion_likelihoods': emotion_likelihoods
        }
    


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

        if response.error.message:
            raise Exception(f'Error during text detection: {response.error.message}')

        # Process or return the detected text annotations
        for text in texts:
            print(f'\n"{text.description}"')

        return texts
    
    async def detect_document_all_text(self, path):
        """Detects document features in an image and returns all text as a single string."""
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = self.image_client.document_text_detection(image=image)   

        all_text = ""
        for page in response.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        word_text = ''.join([
                            symbol.text for symbol in word.symbols   
                        ])
                        all_text += word_text + " "

        return all_text


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

        # Process or return the detected labels
        for label in labels:
            print(f'\n"{label.description}"')

        return labels   