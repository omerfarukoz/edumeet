import base64
import google.generativeai as genai
from backend.google_gemini import AIModels
import asyncio


class Gemini:
    api_key = "AIzaSyAu8tM0uLKv1Ed8P3mnnLM1yKrf25WGLtw"

    if api_key is None:
        print("Error: GEMINI_API_KEY environment variable not set. Please set it.")
        exit(1)

    
    genai.configure(api_key=api_key)

# Maximum number of tokens to generate
# max_output_tokens = 2048  # Set to a higher value for longer outputs

# Controls the randomness of the output
# temperature = 0.7  # Higher values produce more creative, but potentially less relevant, outputs

# Nucleus sampling: only sample from tokens whose probabilities sum up to top_p
# top_p = 0.9  # Lower values produce more focused output

# Sample from the top_k most likely tokens
# top_k = 40  # Higher values produce more diverse output

# Stop generating text after seeing the specified sequence
# stop_sequences = ["\n", "."]  # Stop generation when a new line or period is encountered

# Penalty for repeated sequences
# presence_penalty = 0.6  # Encourage the model to talk about new topics

# Penalty for frequently occurring tokens
# frequency_penalty = 0.2  # Encourage the model to talk about less common topics

# Controls how much the presence and frequency penalties affect generation
# penalty_alpha = 1.0  # Higher values make the penalties more influential

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
        "stream": True, 
    }

   
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # Start chat session
    chat_session = model.start_chat(history=[], )

    async def call_gemini(self, prompt: str):
        try:
            response = self.chat_session.send_message_async(prompt)
            yield response.text

        except Exception as e:  # Catch generic exceptions for broader error handling
            print(f"Error during interaction: {e}")





    async def call_gemini_with_audio(self, audio_file_path: str):

        with open(audio_file_path, "rb") as audio_file:
            base64_audio = base64.b64encode(audio_file.read()).decode('utf-8')

        try:
            response = self.chat_session.send_message(base64_audio)
            yield response.text

        except Exception as e:  # Catch generic exceptions for broader error handling
            print(f"Error during interaction: {e}")


    async def voice_message(self, voice_path):
        upload_file = genai.upload_file(path=voice_path)

        response =  self.model.generate_content(["describe this audio file", upload_file])
        yield response.text