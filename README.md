# 🐦 Sentiment Analysis on Twitter Data 🚀

A Python-based Natural Language Processing (NLP) tool designed to classify text data (tweets) into **Positive** ✅, **Negative** ❌, or **Neutral** ⚖️ categories. This project demonstrates the practical application of NLP libraries like NLTK/TextBlob to analyze social media sentiment.

## 🧐 Overview
The project implements a complete NLP pipeline as outlined in the project requirements:
*   **Data Acquisition** 📥: Processes Twitter-style text data for analysis.
*   **Text Preprocessing** 🧹: Uses Regular Expressions (Regex) to clean noise such as hashtags, mentions, and URLs.
*   **Sentiment Classification** 🧠: Utilizes NLP libraries to determine the polarity of the text.
*   **Visualization** 📊: Generates graphical insights using Matplotlib to show the distribution of sentiments.

## 🛠️ Requirements

You will need Python 3.x installed along with these libraries:

`pip install pandas textblob matplotlib`

## 📈 Usage

1.  **Clone the repository** 📁:
    `git clone [https://github.com/Adarsh12643/twitter-sentiment-analysis.git](https://github.com/Adarsh12643/twitter-sentiment-analysis.git)`
2.  **Navigate to the directory** 📂:
    `cd twitter-sentiment-analysis`
3.  **Run the application** ▶️:
    `python sentiment_analysis.py`

## 🧪 Technical Logic
The tool analyzes the **Polarity** score of each tweet:
*   **Positive** 😊: Polarity score > 0
*   **Neutral** 😐: Polarity score == 0
*   **Negative** ☹️: Polarity score < 0

## 📝 License
Distributed under the MIT License. 📄
