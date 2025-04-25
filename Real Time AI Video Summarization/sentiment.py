from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

def analyze_sentiment(text):
    """
    Runs standard sentiment analysis and returns base label + confidence.
    """
    result = sentiment_pipeline(text[:512])
    label = result[0]["label"]
    score = result[0]["score"]
    return label, round(score, 2)

def map_to_label(base_label, score, text):
    """
    Maps standard sentiment labels to motivational-style labels and emojis.
    """
    text = text.lower()  

    if base_label == "POSITIVE":
        if any(phrase in text for phrase in ["you can do it", "believe", "confidence", "unstoppable"]):
            return "Empowering", "💪"
        elif any(phrase in text for phrase in ["dream", "future", "sky is the limit", "vision"]):
            return "Inspirational", "🚀"
        elif any(phrase in text for phrase in ["lesson", "learn", "understand", "wisdom", "perspective"]):
            return "Insightful", "💡"
        else:
            return "Calming", "😌"

    elif base_label == "NEGATIVE":
        if any(phrase in text for phrase in ["excuse", "stop", "failure", "holding you back"]):
            return "Challenging", "🛑"
        else:
            return "Critical", "⚠️"

    else:  # NEUTRAL
        if any(phrase in text for phrase in ["start today", "now", "immediately"]):
            return "Urgent", "❗"
        else:
            return "Neutral", "⚪"
