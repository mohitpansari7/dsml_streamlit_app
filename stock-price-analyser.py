import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

st.header(
    """
    #Stock Price Analyser
    """
)

ticker_symbol = st.text_input("Enter Stock Symbol", "AAPL", key="placeholder")

col1, col2 = st.columns(2)
#start date of analysis
with col1:
    startDate = st.date_input("Start Date", datetime.date(2019,1,1))
with col2:
    endDate = st.date_input("End Date", datetime.date.today())

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d", start=f"{startDate}", end=f"{endDate}")


st.dataframe(ticker_df)

st.write("""1d closing price chart""")
st.line_chart(ticker_df.Close)
st.write("""Daily Volume Chart""")
st.bar_chart(ticker_df.Volume)
