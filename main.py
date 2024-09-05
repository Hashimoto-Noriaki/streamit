import streamlit as st
import pandas as pd
import numpy as np

st.title('My 1st app')

st.write('データ')
st.write(
    pd.DataFrame({
        '1st columin': [1, 2, 3, 4],
        '2st columin': [10, 20, 30, 40],
    })
)

# チェックボックスがオンの場合のみ DataFrame を表示
if st.checkbox('Show DataFrame'):
    chart_df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_df)
