# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:14:25 2022

@author: Noam
"""
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

header = st.container()
container1 = st.container()
container2 = st.container()
container3 = st.container()

with header:
    st.title('Streamlit is actually pretty cool!')
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
    # you can do data visualization

    you can dislay the table:_.
    '''
    df = pd.DataFrame(np.random.normal(loc=10.0, scale=5.2, size=[600,4]),columns=['a', 'b', 'c','d'])
    c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='d', tooltip=['a', 'b', 'c','d'])
    df
    st.write(c)
    '''
    # let's have a look at some crypto analysis
    '''

# tickerData.info['name']    
temp = pd.read_csv('crypto_ticker_symbols.csv')
crypto_ticker_names = temp['ticker'].tolist()

