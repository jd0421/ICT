import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # 시각화 라이브러리

# Streamlit for sin and cos fuction visualiztion
st.title('Streamlit for sin and cos fuction visualiztion')

x_start = st.slider('x 시작값' ,  0.0, 10.0, 0.0)
x_end = st.slider('x 시작값' ,  10.0, 20.0, 10.0)
x = np.linspace(x_start, x_end)

y_sin = np.sin(x)
y_cos = np.cos(x)


fig , ax = plt.subplots()

ax.plot(x, y_sin)
ax.plot(x, y_cos)
ax.legend(['sin', 'cos'])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('sin and cos fuction')

st.pyplot(fig)

@st.cache
def expensive_computataion(x):
    return np.sin(x) + np.cos(x)

result = expensive_computataion(x)



#1
import plotly.express as px

data_canada = px.data.gapminder().query("country == 'Canada'")
data_canada
fig1 = px.bar(data_canada, x='year' , y='pop')
st.plotly_chart(fig1)


#2
df = px.data.gapminder().query("continent == 'Oceania'")
df
fig2 = px.bar(df, x = 'year' , y = 'pop' , color = 'country' ,
             labels = {'pop' : 'population of Canada'} , hover_data = ['lifeExp','gdpPercap']
             , barmode = 'group')
st.plotly_chart(fig2)


#3
fig3 = px.bar(df, x = 'year' , y = 'pop' , color = 'country' ,
             labels = {'pop' : 'population of Canada'} , hover_data = ['lifeExp','gdpPercap']
             ,pattern_shape_sequence=["."
             ,'+'])
st.plotly_chart(fig3)

#4
import plotly.graph_objs as go
fig4 = go.Figure(data = go.Bar(
    x = [1,2,3,5.5,10],
    y = [10,8,6,4,2],
    width=[0.8,0.8,0.8, 3.5, 4]
))
st.plotly_chart(fig4)

#5
data_canada = px.data.gapminder().query("country == 'Canada'")
data_canada
fig5 = px.line(data_canada, x = 'year', y = 'lifeExp' ,
              title = 'Life expectacy in Canada')
st.plotly_chart(fig5)
