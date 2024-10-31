from backend.google_gemini.service import GoogleGeminiService
from backend.google_vision.service import GoogleVisionService
from backend.redis.service import RedisService
from backend.google_gemini.model import Prompts

import asyncio
import re

class Main:

    gemini: GoogleGeminiService
    google_vision: GoogleVisionService
    redis: RedisService

    def __init__(self):
        self.gemini = GoogleGeminiService()
        self.google_vision = GoogleVisionService()
        self.redis = RedisService()

    # sort out response from Gemini
    def regex_get_answer(self, data: str):
        response = re.findall(r"\{.*?\}", data)
        data = response[0] if response else None


        # clear label data to get tecnichal data
    async def clear_label_data(self,label_data, prompt: Prompts):
        cleared_label_data = await self.gemini.call_gemini(prompt.clear_label_promt, data=label_data)
        self.regex_get_answer(cleared_label_data)
        label_data = cleared_label_data    



    # get data from google vision
    async def detect_emotion_from_image(self,image_path:str):
        emotions_data: list[dict[str,str]] = asyncio.run(self.google_vision.detect_face_emotions(image_path))
        return emotions_data


    async def detect_video_context_from_video(self, video_path:str):
        video_content_data: dict = asyncio.run(self.google_vision.analyze_video(video_path))
        return video_content_data
    
    async def detect_text_from_image(self, image_path:str):

        text_data: list[dict[str,str]] = asyncio.run(self.google_vision.detect_text(image_path))
        return text_data
        
    async def detect_labels_from_image(self, image_path:str):
        label_data: list[dict[str,str]] = asyncio.run(self.google_vision.detect_labels(image_path))
        return label_data
    
    async def detect_document_text(self, document_path:str):
        document_text_data: list[dict[str,str]] = asyncio.run(self.google_vision.detect_document_all_text(document_path))
        return document_text_data


     # analyze all data with gemini and store analyzed data in redis

    async def detect_and_analyze_current_video(self, video_path:str, prompt: Prompts, session_id:str):
        video_content_data = await self.detect_video_context_from_video(video_path=video_path)
        video_response = await self.analyze_text_by_gemini(data=video_content_data, promt=prompt.analyze_video_promt)

        # get spesific answer from response
        self.regex_get_answer(video_response)

        # store response in redis
        self.redis.push(key="video_response", value=video_response, session_id=session_id)


    async def analyze_text_by_gemini(self, promt: Prompts, data: any, session_id:str):
       response = await self.gemini.call_gemini(promt.analyze_text_promt, data=data)


    async def analyze_emotion_by_gemini(self, promt: Prompts, image_path:str):
        data = await self.detect_emotion_from_image(image_path)
        response = await self.gemini.call_gemini(promt.analyze_emotion_promt, data)    

        

    async def analyze_voice_by_gemini(self, promt: Prompts, voice_path:str, session_id:str):
        voice_response = await self.gemini.voice_message(prompt=promt.analyze_voice_promt, voice_path=voice_path)

        # get spesific answer from response
        self.regex_get_answer(voice_response)

        # store voice response in redis
        self.redis.push(key="voice_response", value=voice_response, session_id=session_id)
        return voice_response


    async def detect_and_analyze_current_video(self, video_path:str, prompt: Prompts, session_id:str):
        video_content_data = await self.detect_video_context_from_video(video_path=video_path)
        video_response = await self.analyze_text_by_gemini(data=video_content_data, promt=prompt.analyze_video_promt)

        # get spesific answer from response
        self.regex_get_answer(video_response)

        # store response in redis
        self.redis.push(key="video_response", value=video_response, session_id=session_id)

        return video_response

    async def detect_and_analyze_current_image(self, image_path:str, prompt: Prompts):

        text_data = await self.detect_text_from_image(image_path)
        label_data = await self.detect_labels_from_image(image_path)


        # clear label_data from unrelated labels
        await self.clear_label_data(label_data, prompt.clear_label_promt)
        
        text_and_label_data = (label_data, text_data)

        # analyze data by gemini
        text_response = await self.analyze_text_by_gemini(promt=prompt.analyze_text_and_lable_prompt, data=text_and_label_data)
        emotion_response = await self.analyze_emotion_by_gemini(promt=prompt.analyze_emotion_promt, image_path=image_path)

        # get spesific answer from response
        self.regex_get_answer(text_response)
        self.regex_get_answer(emotion_response)

        # store reposponses in redis
        self.redis.push(key="image_text_response", value=text_response)
        self.redis.push(key="image_emotion_response", value=emotion_response)

        return emotion_response, text_response

    

    # combine all responses and return final response
    async def final_response(self, voice_path:str, image_path:str, video_path:str, prompt: Prompts, session_id:str):

        voice_response = await self.analyze_voice_by_gemini(promt=prompt.analyze_voice_promt, voice_path=voice_path)
        emotion_response, text_response = await self.detect_and_analyze_current_image(image_path, prompt)
        video_response = await self.detect_and_analyze_current_video(video_path, prompt, session_id)

        all_responses = (voice_response, text_response, emotion_response)

        final_response = await self.gemini.call_gemini(prompt.analyze_final_promt, data=all_responses)

        self.regex_get_answer(final_response)
        return final_response

