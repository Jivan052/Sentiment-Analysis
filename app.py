# Author: Jivan Jamdar
# Date: 2023-10-01 Time: 20:57:43PM
# Description: Streamlit app for sentiment analysis using TextBlob and VADER

import streamlit as st
import pandas as pd
import plotly.express as px
from analyzer import SentimentAnalyzer

def main():
    st.set_page_config(
        page_title="Sentiment Analysis App",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("📊 Sentiment Analysis Tool")
    st.write("Analyze the sentiment of tweets, product reviews, or any text!")
    
    analyzer = SentimentAnalyzer()
    
    # different tabs => different functionalities
    tab1, tab2, tab3 = st.tabs(["Single Text Analysis", "Batch Analysis", "About"])
    
    with tab1:
        st.subheader("Single Text Analysis")
        
        # tool selection
        analysis_tool = st.radio(
            "Select analysis tool:",
            ["TextBlob", "VADER"],
            horizontal=True
        )
        
        # text input
        text_input = st.text_area(
            "Enter text to analyze:",
            height=150,
            placeholder="Type or paste your text here..."
        )
        
        if st.button("Analyze Sentiment"):
            if text_input:
                with st.spinner("Analyzing..."):
                    if analysis_tool == "TextBlob":
                        result = analyzer.analyze_textblob(text_input)
                        method = "TextBlob"
                    else:
                        result = analyzer.analyze_vader(text_input)
                        method = "VADER"
                
                # display results with columns
                st.subheader("Results")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"### {result['emoji']} {result['sentiment']}")
                    st.write(f"Analysis method: {method}")
                    
                with col2:
                    if method == "TextBlob":
                        st.metric("Polarity", f"{result['polarity']:.2f}")
                        st.metric("Subjectivity", f"{result['subjectivity']:.2f}")
                    else:  # VADER
                        st.metric("Compound Score", f"{result['compound']:.2f}")
                
                # detailed breakdown for VADER
                if method == "VADER":
                    st.subheader("Sentiment Breakdown")
                    vader_df = pd.DataFrame({
                        'Sentiment': ['Positive', 'Neutral', 'Negative'],
                        'Score': [result['pos'], result['neu'], result['neg']]
                    })
                    
                    fig = px.bar(
                        vader_df, 
                        x='Sentiment', 
                        y='Score',
                        color='Sentiment',
                        color_discrete_map={
                            'Positive': '#2ECC71',
                            'Neutral': '#3498DB',
                            'Negative': '#E74C3C'
                        }
                    )
                    st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("Please enter some text to analyze.")
    
    with tab2:
        st.subheader("Batch Analysis")
        st.write("Upload a CSV or Excel file with a column containing text to analyze multiple entries at once.")
        
        uploaded_file = st.file_uploader("Upload your file", type=["csv", "xlsx"])
        
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith('.csv'):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)
                
                st.write("Preview of uploaded data:")
                st.dataframe(df.head())
                
                text_column = st.selectbox("Select the column containing text to analyze:", df.columns)
                analysis_tool = st.radio(
                    "Select analysis tool for batch processing:",
                    ["TextBlob", "VADER"],
                    horizontal=True
                )
                
                if st.button("Run Batch Analysis"):
                    with st.spinner("Analyzing all entries..."):
                        results = []
                        
                        for text in df[text_column]:
                            if pd.notna(text):  # skip NaN values
                                if analysis_tool == "TextBlob":
                                    result = analyzer.analyze_textblob(str(text))
                                else:
                                    result = analyzer.analyze_vader(str(text))
                                results.append(result)
                            else:
                                # handle NaN values
                                results.append({
                                    'sentiment': 'Unknown',
                                    'emoji': '❓',
                                    'compound' if analysis_tool == "VADER" else 'polarity': 0
                                })
                        
                        # create results DataFrame
                        results_df = pd.DataFrame(results)
                        df_with_sentiment = pd.concat([df, results_df], axis=1)
                        
                        st.subheader("Results")
                        st.dataframe(df_with_sentiment)
                        
                        # download button for results
                        st.download_button(
                            label="Download Results",
                            data=df_with_sentiment.to_csv(index=False),
                            file_name="sentiment_analysis_results.csv",
                            mime="text/csv"
                        )
                        
                        # show summary statistics
                        st.subheader("Sentiment Distribution")
                        sentiment_counts = results_df['sentiment'].value_counts().reset_index()
                        sentiment_counts.columns = ['Sentiment', 'Count']
                        
                        fig = px.pie(
                            sentiment_counts, 
                            names='Sentiment', 
                            values='Count',
                            color='Sentiment',
                            color_discrete_map={
                                'Positive': '#2ECC71',
                                'Neutral': '#3498DB',
                                'Negative': '#E74C3C',
                                'Unknown': '#95A5A6'
                            }
                        )
                        st.plotly_chart(fig, use_container_width=True)
                
            except Exception as e:
                st.error(f"Error processing the uploaded file: {str(e)}")
    
    with tab3:
        st.subheader("About This App")
        st.write("""
        This Sentiment Analysis App uses two popular techniques:
        
        1. **TextBlob**: A simple NLP library that provides a simple API for diving into common NLP tasks.
           - Polarity: Score from -1 (very negative) to +1 (very positive)
           - Subjectivity: Score from 0 (objective) to 1 (subjective)
        
        2. **VADER** (Valence Aware Dictionary and sEntiment Reasoner): A lexicon and rule-based sentiment analysis tool specifically attuned to sentiments expressed in social media.
           - Compound: Normalized score from -1 (very negative) to +1 (very positive)
           - Positive, Neutral, Negative: Proportions of text that fall in each category
        
        ### When to use each tool:
        - TextBlob is simpler and works well for general text
        - VADER is better for social media content, slang, and emoticons
        
        ### Limitations:
        - Neither tool understands sarcasm well
        - Context is often missed
        - Language specific (works best with English)
        """)

if __name__ == "__main__":
    main()