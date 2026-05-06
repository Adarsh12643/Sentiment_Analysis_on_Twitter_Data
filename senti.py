import pandas as pd
import re
from textblob import TextBlob
import matplotlib.pyplot as plt

# 1. Sample Data (Twitter-like tweets)
data = {
    'Tweets': [
        "I love the new features of this AI, it's amazing!",
        "The update is okay, but it has some bugs.",
        "I hate the new interface, it's very confusing and slow.",
        "Today is a normal day, nothing special.",
        "Absolutely fantastic experience! Highly recommended.",
        "Worst service ever. I am very disappointed.",
        "The weather is fine today."
    ]
}

df = pd.DataFrame(data)

# 2. Data Cleaning Function
def clean_tweet(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) # Remove mentions
    text = re.sub(r'#', '', text)             # Remove hashtags
    text = re.sub(r'RT[\s]+', '', text)       # Remove retweets
    text = re.sub(r'https?:\/\/\S+', '', text) # Remove links
    return text

df['Cleaned_Tweets'] = df['Tweets'].apply(clean_tweet)

# 3. Sentiment Analysis Function
def get_sentiment(text):
    analysis = TextBlob(text)
    # Score is between -1 (negative) and 1 (positive)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

df['Sentiment'] = df['Cleaned_Tweets'].apply(get_sentiment)

# 4. Results
print(df[['Tweets', 'Sentiment']])

# 5. Visualization
sentiment_counts = df['Sentiment'].value_counts()
plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar', color=['green', 'blue', 'red'])
plt.title('Sentiment Analysis Results')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.xticks(rotation=0)
plt.show()