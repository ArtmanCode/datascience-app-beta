import yfinance as yf
import streamlit as st

st.write("""
# Gráfico das Ações da Google
1. Preço de fechamento(Close) e 2. Volume
""")


tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2015-5-31', end='2021-5-10')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)