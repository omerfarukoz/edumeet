from pydantic import BaseModel, Field

class TextResponse(BaseModel):
    text: str


class LabelAnnotation(BaseModel):
    description: str
    score: float = None
    top: float = None  
    left: float = None
    right: float = None
    bottom: float = None

class ImageLabelResponse(BaseModel):
    labels: list[LabelAnnotation]


class EmotionLikelihood(BaseModel):
    emotions: dict[str, str]

    
class VideoAnalysisResult(BaseModel):
    face_count: int = Field(ge=0)
    likelihood_name: str
    emotion_likelihoods: list[EmotionLikelihood] = Field(default_factory=list)





