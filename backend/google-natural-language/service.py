from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def analyze_document(text):
    """Analyzes a document and extracts key information."""
    client = language.LanguageServiceClient()

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    

    sentiment = client.analyze_sentiment(document=document).document_sentiment

    entities = client.analyze_entities(document=document).entities

    categories = client.classify_text(document=document).categories

    return {
        "sentiment": sentiment,
        "entities": entities,
        "categories": categories
    }

# Makale metnini buraya ekleyin
text = """
# Makale metni buraya gelecek
"""

analyze_document(text)