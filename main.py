import streamlit as st
import datetime
import pandas as pd
import yfinance as yf
import cufflinks as cf

st.title('Stock Price App')

# Sidebar
st.sidebar.subheader('Query parametrs')
start_date = st.sidebar.date_input('Start date', datetime.date(2020, 1, 1))
end_date = st.sidebar.date_input('End date', datetime.date(2021, 1, 31))

# Get ticker data
ticker_list = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/s-and-p-500-companies/master/data/constituents_symbols.txt')
ticker_symbol = st.sidebar.selectbox('Stock ticker', ticker_list)
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period='1d', start=start_date, end=end_date)

# Ticker information
string_logo = '<img src=%s>' % ticker_data.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

ticker_name = ticker_data.info['longName']
st.header('**%s**' % ticker_name)

string_summary = ticker_data.info['longBusinessSummary']
st.info(string_summary)

# Ticker data
st.header('**Ticker data**')
st.write(ticker_df)

# Bolliger bands
st.header('**Bollinger bands**')
qf = cf.QuantFig(ticker_df, title='First Quant Figure', legend='top', name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)