from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import predict_comment

app = FastAPI()

# CORS fix (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body schema
class Comment(BaseModel):
    text: str

# Root route (prevents "Not Found" confusion)
@app.get("/")
def home():
    return {"message": "Bad Comment Detector API is running 🚀"}

# Prediction route
@app.post("/predict")
async def predict(comment: Comment):
    pred, prob = predict_comment(comment.text)

    return {
        "comment": comment.text,
        "result": "Bad ❌" if pred == 1 else "Good ✅",
        "confidence": round(prob * 100, 2)
    }