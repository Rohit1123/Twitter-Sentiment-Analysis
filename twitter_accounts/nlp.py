import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

def sentiment_analysis(input_txt: str):
    s = SentimentIntensityAnalyzer()
    score = s.polarity_scores(input_txt)
    print(score)
    return score