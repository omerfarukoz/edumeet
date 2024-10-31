from pydantic import BaseModel, Field

class Prompts(BaseModel):
    

    text_and_lable_text: str = """
    aşağıdaki label ve text incele ve şıklardan birini seç
    cevap türkçe olsun
    verdiğim formatta yanıt ver

    label ve text arasında hiç uyum varsa ->
    {
    "State":"1",
    "Question": <text ile ilgili teknik soru yarat>
    }

    label ve text arasında hiçbir uyum yoksa ->
    {
    "State":"2",
    "issue": <spesifik sebep belirt>
    }

    bilgi yanlışlığı varsa ->
    {
    "state":"3",
    "wrong_information": <yanlışı belirt>
    }
    """


    emotion_text: str = """
    bu veriye bakarak şu formatta cevap ver
    {
    "emotion": < duyguyu yaz>
    }
""" 

    voice_text: str = """"

    Ses kaydında anlatılanları anla ve şu formatta cevap ver - >
{
“topic”: < buraya konuyu yaz >
“speaker_state”: < konuşan kişinin konuşma biçimindeki duyguyu yaz>,
“information”: {
“information_accuracy”: < True or False yaz >,
“question”: < konu ile ilgili teknik soru yaz >,
“wrong_information: < eğer yanlış bilgi varsa buraya yaz >
}
}
    """


    video_text: str = """
sırasıyla label, text, speech verisi var
verdiğim formatta yanıt ver
cevap türkçe olsun


Veri arasında %50 üzerinde uyum varsa ->
{
“State”:”1”,
“Question”: <text ile ilgili teknik soru yarat>
}


Data arasında %50 üzerinde uyum yoksa -> 
{
“State”:”2”,

“issue”: <spesifik sebep belirt>
}

Data arasında yanlış bilgi varsa ->
{
"state":"3",
"wrong_information": <yanlışı belirt>
}
"""

    final_text: str = """"
    dataları anlamlı ve kısa şekilde birleştir ve şu formatta soru ya da wrong information belirt -> 
{
“final_response”: < response >
}
    """

    clear_label_text: str = """
bu label data dan teknik olmayan şeyleri çıkar ve şu formatta yanıt ver ->
{
"labels": []
}
"""

    analyze_emotion_promt: str = Field(emotion_text, description="Emotion prompt for Gemini")
    analyze_voice_promt: str = Field(voice_text, description="Voice prompt for Gemini")
    analyze_document_promt: str = Field("analyze document", description="Document prompt for Gemini")
    analyze_text_promt: str = Field("analyze text", description="Text prompt for Gemini")
    analyze_text_and_lable_prompt: str = Field(text_and_lable_text, description="Text and label prompt for Gemini")
    analyze_final_promt: str = Field(final_text, description="Final prompt for Gemini")
    analyze_video_promt: str = Field(video_text, description="Video prompt for Gemini")
    clear_label_promt: str = Field(clear_label_text, description="Clear label prompt for Gemini")