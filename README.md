# claimbridge-ai-api
AI-based heir prediction for ClaimBridge
# ClaimBridge AI Prediction API

This FastAPI app provides heir prediction logic based on relation and age.

## Endpoints

- `GET /` - Health check
- `POST /predict` - Predict heir status

### Example Input:
```json
{
  "name": "Meera Singh",
  "relation": "child",
  "age": 28
}

