# -*- coding:utf-8 -*-
"""
作者：tongsiwen
日期：2024年07月18日
"""
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')
# 样例 1

st.write('Hello, *World!* :sunglasses:')
# 样例 2

st.write(1234)
# 样例 3

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [20, 10, 30, 40]
})
st.write(df)
# 样例 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
# 样例 5


# 创建一个包含200行3列的随机数据的DataFrame
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
# 使用Altair创建一个散点图
c = alt.Chart(df2).mark_circle().encode(
    x='a',
    y='b',
    size='c',
    color='c',
    tooltip=['a', 'b', 'c'])
# 使用Streamlit显示图表
st.write(c)

st.write(df2)
