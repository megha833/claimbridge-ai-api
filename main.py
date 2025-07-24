from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression
import pandas as pd

# ----------------- Sample ML Setup ---------------------
# Training data (dummy data for demo)
data = pd.DataFrame({
    "relation": ["spouse", "child", "parent", "sibling", "uncle", "spouse", "child"],
    "age": [40, 22, 65, 33, 55, 45, 19],
    "is_heir": [1, 1, 0, 0, 0, 1, 1]
})
data["relation_encoded"] = data["relation"].astype("category").cat.codes
X = data[["age", "relation_encoded"]]
y = data["is_heir"]
model = LogisticRegression().fit(X, y)

# ----------------- API Setup ---------------------
class Claimant(BaseModel):
    name: str
    relation: str
    age: int

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.post("/predict")
def predict_heir(claimant: Claimant):
    encoded_relation = pd.Series([claimant.relation]).astype("category").cat.codes[0]
    X_input = [[claimant.age, encoded_relation]]
    
    prediction = model.predict(X_input)[0]
    confidence = model.predict_proba(X_input)[0][1]

    result = {
        "heir": claimant.name if prediction == 1 else "Not predicted as heir",
        "confidence_score": round(confidence, 2),
        "relation": claimant.relation
    }
    return result
