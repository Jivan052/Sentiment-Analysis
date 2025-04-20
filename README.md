# 💬 Sentiment Analysis Tool

A powerful web application for analyzing sentiment in text data using multiple NLP techniques.

![image](https://github.com/user-attachments/assets/e9fae115-58c0-48d7-992f-fef2c0473443)

---

## 📝 Overview

This tool helps you analyze the sentiment (positive, negative, or neutral) of any text content such as tweets, product reviews, customer feedback, etc. It provides both single text analysis and batch processing capabilities with interactive visualizations.

---

## 🚀 Features

### 🔍 Dual Analysis Methods

- **TextBlob**: Simple and effective general-purpose sentiment analysis  
- **VADER**: Specialized for social media content and colloquial expressions

### ✏️ Single Text Analysis
![image](https://github.com/user-attachments/assets/bb7504da-7a0d-41d2-89f1-6f90bbdf7e95)

- Instant sentiment classification  
- Sentiment scores with detailed breakdown  
- Visual representation of results

### 📁 Batch Processing
![image](https://github.com/user-attachments/assets/9ce56588-d4be-4eca-b6ae-b48a83dad0d9)

- Upload CSV or Excel files with multiple text entries  
- Process hundreds of entries at once  
- Download results as a CSV file  
- Visualize sentiment distribution across all entries

### 🧑‍💻 Interactive UI

- User-friendly interface  
- Real-time analysis  
- Interactive charts and visualizations

---

## ⚙️ Installation

### Clone this repository

```bash
git clone https://github.com/your-username/sentiment-analysis.git
cd Sentiment-Analysis
```
### Install the required dependencies
```bash
pip install -r requirements.txt
```
## ▶️ Usage
### Run the Streamlit app
```bash
streamlit run app.py
```
Then open your web browser and navigate to:
http://localhost:8501

## 🧭 How to Use

### 🔹 For Single Text Analysis
- Enter or paste your text  
- Select your preferred analysis method (**TextBlob** or **VADER**)  
- Click **"Analyze Sentiment"**

### 🔹 For Batch Analysis
- Upload a CSV or Excel file with text data  
- Select the text column to analyze  
- Choose your analysis method  
- Click **"Run Batch Analysis"**

---

## 📊 Understanding the Results

### 📘 TextBlob Analysis
- **Polarity**: Score from **-1.0** (very negative) to **1.0** (very positive)  
- **Subjectivity**: Score from **0.0** (objective) to **1.0** (subjective)

### 🐦 VADER Analysis
- **Compound Score**: Normalized score between **-1** (very negative) and **1** (very positive)  
- **Positive / Neutral / Negative**: Proportion of text falling into each category

---

## 📦 Dependencies

- `streamlit >= 1.24.0`  
- `textblob >= 0.17.1`  
- `vaderSentiment >= 3.3.2`  
- `pandas >= 2.0.3`  
- `matplotlib == 3.7.2`  
- `plotly >= 5.15.0`

---

## 💡 Use Cases

- Monitor brand sentiment on social media  
- Analyze customer reviews and feedback  
- Track public opinion on products or services  
- Research emotional content in texts  
- Evaluate communication effectiveness

---

## ⚠️ Limitations

- Best performance with English text  
- May struggle with sarcasm and complex context  
- Limited understanding of industry-specific terminology  
- Cannot detect subtle emotional nuances

#### Here is the Deployed Link: https://huggingface.co/spaces/Jivan01/Sentiment_Analysis
Follow me on [Hugging Face](https://huggingface.co/Jivan01)
**Created with ❤️ by [Jivan Jamdar](https://github.com/Jivan052)**
