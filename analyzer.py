from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        self.vader = SentimentIntensityAnalyzer()
    
    def analyze_textblob(self, text):
        """Analyze text sentiment using TextBlob"""
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        
        # sentiment category
        if polarity > 0.05:
            sentiment = "Positive"
            emoji = "😃"
        elif polarity < -0.05:
            sentiment = "Negative"
            emoji = "😞"
        else:
            sentiment = "Neutral"
            emoji = "😐"
        
        return {
            "sentiment": sentiment,
            "polarity": polarity,
            "emoji": emoji,
            "subjectivity": analysis.sentiment.subjectivity
        }
    
    def analyze_vader(self, text):
        """Analyze text sentiment using VADER"""
        scores = self.vader.polarity_scores(text)
        
        # determine sentiment category based on compound score
        if scores["compound"] >= 0.05:
            sentiment = "Positive"
            emoji = "😃"
        elif scores["compound"] <= -0.05:
            sentiment = "Negative"
            emoji = "😞"
        else:
            sentiment = "Neutral"
            emoji = "😐"
        
        return {
            "sentiment": sentiment,
            "compound": scores["compound"],
            "pos": scores["pos"],
            "neu": scores["neu"],
            "neg": scores["neg"],
            "emoji": emoji
        }