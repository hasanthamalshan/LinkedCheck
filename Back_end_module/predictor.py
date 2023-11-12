import joblib
import pandas as pd
from pydantic import BaseModel

class Item(BaseModel):
    employment_type: str
    required_experience: str
    character_count: int
    title: str

loaded_model = joblib.load('trained_model/nb_classifier.joblib')
loaded_preprocessor = joblib.load('trained_model/preprocessor.joblib')

def predict(item: Item):
    new_data = pd.DataFrame([item])
    new_data_combined = loaded_preprocessor.transform(new_data)

    predictions = loaded_model.predict(new_data_combined)

    return bool(predictions[0])