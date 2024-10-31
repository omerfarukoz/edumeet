import base64
import google.generativeai as genai
import asyncio
import os
from model import Prompts




class GoogleGeminiService:
    api_key = os.getenv("GEMINI_API_KEY")

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
        "temperature": 0.3,
        "top_p": 0.3,
        "top_k": 10,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[], )

    async def call_gemini(self, prompt: str, data = None):
        try:
            response = self.chat_session.send_message(prompt + "\n" + data)
            print(response.text)
            return response.text
        
        except ValueError as e:
            print(f"Invalid input: {e}")
        
        except Exception as e:
            print(f"Unexpected error: {e}")


    async def voice_message(self, prompt: str, voice_path: str):
        upload_file = genai.upload_file(path=voice_path)

        response =  self.model.generate_content([prompt, upload_file])
        print(response.text)
        return response.text

