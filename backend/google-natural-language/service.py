from google.cloud import language
from google.cloud import language

class GoogleNaturalLanguageService:

    client = language.LanguageServiceClient()
    
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


if __name__ == "__main__":
    text = "This is a sample text for sentiment analysis. and more and more words for testing the entity analysis."
    result = GoogleNaturalLanguageService().analyze_document(text)
    print(result)