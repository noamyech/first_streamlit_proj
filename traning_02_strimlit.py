# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:14:25 2022

@author: Noam
"""
# import yfinance as yf
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import datetime


header = st.container()
container1 = st.container()
container2 = st.container()
container3 = st.container()

with header:
    '''
    # welcome to noam's pathetic app :sleeping:
    '''
    st.header('Streamlit is actually pretty cool!')
    st.header("Here I'll show you why")
with container1:
    "you can actually insert equations:"
    st.latex("\Delta^2 f/\dot\phi\cdot A=\int a x^2\,dx")
with container2:
    "or if you are in a mood for party"
    clicked=st.button("release baloons")
    if clicked:
        st.balloons()
    st.header('Time to face yourself')
    "are you a robot?"
    checked=st.checkbox("I think that I am not a robot")
    if checked:
        st.write("Wrong! :monkey:")
        '**Try again**'
        choice=st.radio('what are you?',['None','robot','loser'])
        if choice=='robot':
            "*** NOPE ***"
        if choice=='loser':
             "Damm right you are :heart:"
with container3:
    '''
    # It can do data visualization

    you can dislay the table:
    '''
    df = pd.DataFrame(np.random.normal(loc=10.0, scale=5.2, size=[600,4]),columns=['a', 'b', 'c','d'])
    c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='d', tooltip=['a', 'b', 'c','d'])
    df
    '''
    as:
    '''
    st.write(c)
    '''
    # let's have a look at some crypto
    '''

# tickerData.info['name']    
temp = pd.read_csv('crypto_ticker_symbols.csv')
crypto_ticker_names = temp['ticker'].tolist()
# crypto_common_names = temp['name'].tolist()



# data_df = yf.download(crypto_ticker_names)
# data_df.to_pickle('data_df.pkl')

                    
data_df= pd.read_pickle("data_df.pkl")
                    

# =============================================================================
# 
# #define the ticker symbol
# tickerSymbol = 'BTC-USD'
# #get data on this ticker
# tickerData = yf.Ticker(tickerSymbol)
# #get the historical prices for this ticker
# tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# # Open	High	Low	Close	Volume	Dividends	Stock Splits
# 
# =============================================================================

options = st.multiselect(
     'what crypto to display?',crypto_ticker_names,['BTC-USD','ETH-USD'])



col1, col2 = st.columns(2)

with col1:
    st.header("start date")    
    d_start = st.date_input(" ",datetime.date(2014, 1, 1))
with col2:
    st.header("end date")
    d_end   = st.date_input(" ",datetime.date(2022, 1, 1))

dd_end=datetime.datetime(year=d_end.year,month=d_end.month,day=d_end.day,hour=0,minute=0)
dd_start=datetime.datetime(year=d_start.year,month=d_start.month,day=d_start.day,hour=0,minute=0)


# range_condition=df[‘Color’] == ‘Green’


# table_time_raw=data_df.index

# table_time_fixed=table_time_raw.date
# df.loc[df[‘Color’] == ‘Green’]



# in_date_range=(data_df.index >= dd_start) & (data_df.index <= dd_end)
data_df_sliced=data_df.loc[(data_df.index >= dd_start) & (data_df.index <= dd_end)]

close_df  = data_df_sliced.Close[options]
volume_df = data_df_sliced.Volume[options]

clicked=st.button("reset date range")
if clicked:
    close_df  = data_df.Close[options]
    volume_df = data_df.Volume[options]
    
st.write("""
## Closing Price
""")
st.line_chart(close_df)
st.write("""
## Volume Price
""")
st.line_chart(volume_df)


    
    
    
    
