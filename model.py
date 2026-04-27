from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Training data
comments = [
    "I love this", "Great work", "Amazing project",
    "You are stupid", "I hate you", "Idiot",
    "Very nice", "Well done", "Keep it up",
    "Dumb fellow", "Worst thing ever"
]

labels = [0,0,0, 1,1,1, 0,0,0, 1,1]  # 1 = Bad

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(comments)

model = LogisticRegression()
model.fit(X, labels)

def predict_comment(text):
    X_test = vectorizer.transform([text])
    pred = model.predict(X_test)[0]
    prob = model.predict_proba(X_test)[0][pred]
    return pred, prob