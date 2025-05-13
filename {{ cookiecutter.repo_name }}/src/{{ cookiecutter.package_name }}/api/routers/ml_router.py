# ml_router.py
from fastapi import APIRouter
from ...models.ml.classification.model import ClassificationModel
from ...api.models import TextGenerationRequest, TextGenerationResponse

router = APIRouter(prefix="/ml", tags=["ML"])

model = ClassificationModel()

@router.post("/predict", response_model=TextGenerationResponse)
def predict(request: TextGenerationRequest):
    """
    Predict using a dummy classification model.
    """
    prediction = model.predict(request.prompt)
    return TextGenerationResponse(result=str(prediction))
