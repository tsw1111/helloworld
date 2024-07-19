# -*- coding:utf-8 -*-
"""
作者：tongsiwen
日期：2024年07月19日
"""
import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')
chart_data = pd.DataFrame(
     np.random.randn(100, 4),   # 0~99 一共100个数据，共有四组
     columns=['a', 'b', 'c', 'd'])
my_table = st.table(chart_data)
st.line_chart(chart_data)




chart_data = pd.DataFrame(
   {
       "col1": np.random.randn(50),
       "col2": np.random.randn(50),
       "col3": np.random.choice(["A", "B", "C"], 50),
   }
)
my_table = st.table(chart_data)
st.line_chart(chart_data, x="col1", y="col2", color="col3")




chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["col1", "col2", "col3"])
my_table = st.table(chart_data)
st.line_chart(
   chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
)



df1 = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
my_table = st.table(df1)
my_chart = st.line_chart(df1)

