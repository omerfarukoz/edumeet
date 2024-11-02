from google.cloud import language
from google.cloud import language

class GoogleNaturalLanguageService:

    # This class is a wrapper for the Google Natural Language API.
    # It provides methods for sentiment analysis, entity extraction, and text classification.
    # It returns a dictionary containing the sentiment score, entities, and categories of the input text.

    def __init__(self):
        self.client = language.LanguageServiceClient()
    
    def analyze_document(self,text):
    
        document = language.Document(
            content=text,
            type=language.Document.Type.PLAIN_TEXT)
        

        sentiment = self.client.analyze_sentiment(document=document).document_sentiment

        entities = self.client.analyze_entities(document=document).entities

        categories = self.client.classify_text(document=document).categories

        return {
            "sentiment": sentiment,
            "entities": entities,
            "categories": categories
        }
