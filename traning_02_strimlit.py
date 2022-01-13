import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

header = st.container()
container1 = st.container()
	@@ -38,12 +41,88 @@
             "Damm right you are :heart:"
with container3:
    '''
    # data visualization
    you can dislay the table:_.
    '''
    df = pd.DataFrame(np.random.normal(loc=10.0, scale=5.2, size=[600,4]),columns=['a', 'b', 'c','d'])
    c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='d', tooltip=['a', 'b', 'c','d'])
    df
    st.write(c) 
