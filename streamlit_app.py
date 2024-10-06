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

#6
df_1 = px.data.gapminder().query("continent == 'Oceania'")
df_1
fig6 = px.line(df_1, x = 'year', y = 'pop' , color ='country' , symbol='country')
st.plotly_chart(fig6)

#7 piecharts
df_2 = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df_2
fig7 = px.pie(df_2, values = 'pop',  names = 'country' , title = 'population of European contintent')
st.plotly_chart(fig7)

#8 donut chart
labels = ['A','B', 'C' ,'D']
values = [300,200,100,500]
fig8 = go.Figure(data = [go.Pie(labels = labels, values = values, hole=.3)]) # hole 도넛차트 구현
st.plotly_chart(fig8)

#9 donut chart_specific
fig9 = go.Figure(data = [go.Pie(labels = labels, values = values, pull = [0 , 0, 0.2,0])])
st.plotly_chart(fig9)

#10 heatmaps

fig10 = px.imshow([[1,23,49],[123,5,4],[45,6,3]]
                )
st.plotly_chart(fig10)


#11 boxplots
df_3 = px.data.tips()
df_3
fig11 = px.box(df_3, y = 'total_bill' , x = 'time' , points = 'all' , color = 'smoker')
st.plotly_chart(fig11)

#12 boxplots_details
fig12 = px.box(df_3, y = 'total_bill' , x = 'day' , points = 'all' , color = 'smoker')
st.plotly_chart(fig12)

#13 bubble charts
df_4 = px.data.gapminder()
df_4
fig13 = px.scatter(df_4.query("year == 2007"), x = 'gdpPercap' , y = 'lifeExp', size = 'pop', color = 'continent')
st.plotly_chart(fig13)

#14 Treemap
df_5 = px.data.gapminder().query("year == 2007")
df_5
fig14 = px.treemap(df_5, path=[px.Constant('World'), 'continent','country'], values = 'pop' , color = 'lifeExp')
st.plotly_chart(fig14)


#Plotly시각화 상.ipynb
#fig_15_barchart
#-width = 가로 크기 조절
#-height = 세로 크기 조절
fig15 = px.bar(x=["a", "b", "c"], y=[1, 3, 2], width = 600, height = 400)
st.plotly_chart(fig15)

