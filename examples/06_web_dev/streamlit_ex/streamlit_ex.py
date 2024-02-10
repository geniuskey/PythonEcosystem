"""
실행 방법:
> pip install streamlit pandas numpy
> streamlit run streamlit_ex.py
"""
import streamlit as st
import pandas as pd
import numpy as np

# 타이틀 설정
st.title('My first Streamlit app')

# 데이터 생성
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c'])

# 데이터 표시
st.write("Here's our first attempt at using data to create a table:")
st.write(data)

# 차트 그리기
st.line_chart(data)
