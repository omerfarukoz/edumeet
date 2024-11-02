from google_gemini.service import GoogleGeminiService
from google_vision.service import GoogleVisionService
from redis.service import RedisService
from google_gemini.model import Prompts
from google_text_to_speech.service import GoogleTextToSpeechService

import re
import json

class Main:

    gemini: GoogleGeminiService
    google_vision: GoogleVisionService
    google_tts: GoogleTextToSpeechService
    # redis: RedisService

    def __init__(self):
        self.gemini = GoogleGeminiService()
        self.google_vision = GoogleVisionService()
        self.google_tts = GoogleTextToSpeechService()

        # self.redis = RedisService()

    # Sort out response from Gemini


    def regex_get_answer(self, data: any):
        if data is None:
            return None
        # Convert to string if it's not already
        if not isinstance(data, str):
            data = str(data)
        
        # Replace non-standard quotes with standard quotes
        data = data.replace("“", "\"").replace("”", "\"")
        
        # Regex to find content inside braces
        response = re.findall(r"(\{.*?\})", data, re.DOTALL)
        
        data = response[0]
        
        # Return the first match if it exists, else return None
        return response[0] if response else None

    def parse_json(self, data: str):
    # Replace curly quotes with standard quotes
        data = data.replace("“", "\"").replace("”", "\"")
        
        try:
            # Attempt to parse JSON directly
            response_dict = json.loads(data)
            return response_dict
        except json.JSONDecodeError as e:
            return None

    # Clear label data to get technical data
    async def clear_label_data(self, label_data: any, prompt: Prompts):
        cleared_label_data = await self.gemini.call_gemini(prompt.clear_label_prompt, data=label_data)
        self.regex_get_answer(cleared_label_data)
        label_data = cleared_label_data    

    # Get data from Google Vision
    async def detect_emotion_from_image(self, image_path: str):
        emotions_data = await self.google_vision.detect_face_emotions(image_path)
        return emotions_data

    async def detect_video_context_from_video(self, video_path: str):
        video_content_data = await self.google_vision.analyze_video(video_path)
        return video_content_data
    
    async def detect_text_from_image(self, image_path: str):
        text_data = await self.google_vision.detect_text(image_path)
        return text_data
        
    async def detect_labels_from_image(self, image_path: str):
        label_data= await self.google_vision.detect_labels(image_path)
        return label_data
    
    async def detect_document_text(self, document_path: str):
        document_text_data = await self.google_vision.detect_document_all_text(document_path)
        return document_text_data

    # Analyze all data with Gemini and store analyzed data in Redis
    async def detect_and_analyze_current_video(self, video_path: str, prompt: Prompts, session_id: str):
        video_content_data = await self.detect_video_context_from_video(video_path=video_path)
        video_response = await self.analyze_text_by_gemini(data=video_content_data, promt=prompt.analyze_video_promtp)

        # Get specific answer from response
        self.regex_get_answer(video_response)

        # Store response in Redis
        # self.redis.push(key="video_response", value=video_response, session_id=session_id)

    async def analyze_text_by_gemini(self, promt: str, data: any):
        response = await self.gemini.call_gemini(promt, data=data)

    async def detec_and_analyze_emotion_by_gemini(self, promt: str, image_path: str):
        data = await self.detect_emotion_from_image(image_path)
        response = await self.gemini.call_gemini(promt, data)    

    async def analyze_voice_by_gemini(self, prompt: Prompts, voice_path: str):
        voice_response = await self.gemini.voice_message(prompt=prompt.analyze_voice_prompt, voice_path=voice_path)

        # Get specific answer from response
        self.regex_get_answer(voice_response)

        # Store voice response in Redis
        # self.redis.push(key="voice_response", value=voice_response, session_id=session_id)
        return voice_response

    async def detect_and_analyze_current_video(self, video_path: str, prompt: Prompts, session_id: str):
        video_content_data = await self.detect_video_context_from_video(video_path=video_path)
        video_response = await self.analyze_text_by_gemini(data=video_content_data, promt=prompt.analyze_video_promt)

        # Get specific answer from response
        self.regex_get_answer(video_response)

        # Store response in Redis
        # self.redis.push(key="video_response", value=video_response, session_id=session_id)

        return video_response

    async def detect_and_analyze_current_image(self, image_path: str, prompt: Prompts):
        text_data = await self.detect_text_from_image(image_path)
        label_data = await self.detect_labels_from_image(image_path)

        # Clear label_data from unrelated labels
        await self.clear_label_data(label_data, prompt)
        
        text_and_label_data = {
            "label_data": label_data,
            "text_data": text_data,
        }

        # Analyze data by Gemini
        text_response = await self.analyze_text_by_gemini(promt=prompt.analyze_text_and_lable_prompt, data=text_and_label_data)
        emotion_response = await self.detec_and_analyze_emotion_by_gemini(promt=prompt.analyze_emotion_prompt, image_path=image_path)

        # Get specific answer from response
        self.regex_get_answer(text_response)
        self.regex_get_answer(emotion_response)

        # Store responses in Redis
        # self.redis.push(key="image_text_response", value=text_response)
        # self.redis.push(key="image_emotion_response", value=emotion_response)

        return (emotion_response, text_response)

    # Combine all responses and return final response
    async def final_response(self, voice_path: str, image_path: str, video_path: str, prompt: Prompts):
        voice_response = await self.analyze_voice_by_gemini(prompt=prompt, voice_path=voice_path)
        (emotion_response, text_response) = await self.detect_and_analyze_current_image(image_path, prompt)
        # video_response = await self.detect_and_analyze_current_video(video_path, prompt, session_id)

        all_responses = {
            "emotion_data": emotion_response,
            "text_and_label_data": text_response,
            "voice_data": voice_response,
        }
        final_response = await self.gemini.call_gemini(prompt.analyze_final_prompt, data=all_responses)

        self.regex_get_answer(final_response)

        if final_response:
            final_response =self.regex_get_answer(data=final_response)
            try:
                final_response = self.parse_json(final_response)
                await self.google_tts.generate_audio(final_response["final_response"], "speak")
            except (Exception) as e:
                print("Error parsing final_response or missing 'final_response' key:", e)
        else:
            print("Final response is None or empty")


        return final_response
