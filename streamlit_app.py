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

# Plotly시각화 상.ipynb
#fig15_barchart
#-width = 가로 크기 조절
#-height = 세로 크기 조절

st.title("Plotly시각화 상.ipynb")
st.text("fig_15_barchart")
st.text("-width = 가로 크기 조절")
st.text("-height = 세로 크기 조절")

fig15 = px.bar(x=["a", "b", "c"], y=[1, 3, 2], width = 600, height = 400)
st.plotly_chart(fig15)

#fig16_margin
st.text("fig16_margin")

fig16 = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig16.update_layout(
    width = 600,
    height = 400,
    margin_l =50, #
    margin_r =50, #
    margin_t =100, #
    margin_b =100 #
)

st.plotly_chart(fig16)

#fig17_title_in_chart
st.markdown("""
    ---
    fig17_title_in_chart
    """)
fig17 = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig17.update_layout( title_text = 'Bar Chart') #title_text =
st.plotly_chart(fig17)

#fig18
st.markdown("""
    ---
    - Express 사용법
    - Graph object 사용법
    """)

import plotly.graph_objects as go
fig18 = go.Figure(go.Bar(x=['A','B','C'], y = [1,3,2]))
st.plotly_chart(fig18)

#fig19
st.markdown("""
---
Font 스타일 지정 (색, 서체, 크기)
""")

fig19 = px.bar(x=["a", "b", "c"], y=[1, 3, 2], title = 'Bar Chart') #title =
fig19.update_layout(
    title_y = 0.9, # 0~1 1은 맨 윗쪽
    title_x = 0.5, # 0~1 1은 맨 오른쪽
    title_xanchor = 'center',
    title_yanchor = 'middle',

    #폰트 스타일 추가
    title_font_size = 50,
    title_font_family = 'Times', #일반적인 기본글꼴 적용
    title_font_color = 'red'
)
st.plotly_chart(fig19)

#fig20
st.markdown("""
---
축타이틀 설정
""")
df_6 = px.data.tips()
df_6
fig20 = px.scatter(df_6, x = 'total_bill', y = 'tip') #축이름 설정  x = 'total_bill', y = 'tip'
st.plotly_chart(fig20)

st.markdown("""
    - 축이름 설정  x = 'total_bill', y = 'tip'
    - 산점도
    - 가로축 : 값정보(수치)
    - 세로축 : 값정보(수치)
    - 가로축과 세로축간에 어떤 관계 , 경향을 보이는지 체크가능
""")

#fig21_scatter_colored
# used df_6

st.markdown("""
---
fig21_scatter_colored
""")
fig21 = px.scatter(df_6, x = 'total_bill', y = 'tip', color = 'sex') #축 설정  x = 'total_bill', y = 'tip'
st.plotly_chart(fig21)
st.markdown("""
---
    - 축 설정  x = 'total_bill', y = 'tip'
""")


#fig22_scatter_colored_with_unit
# used df_6
st.markdown("""
---
fig22_scatter_colored_with_unit
""")

fig22 = px.scatter(df_6, x = 'total_bill', y = 'tip', color = 'sex',
                 labels = dict(total_bill ='total_bill($)' ,tip = 'tip($)' ) )
#축레이블 설정  labels = dict(total_bill ='total_bill($)' ,tip = 'tip($)'
st.plotly_chart(fig22)
st.markdown("""
---
    - 축레이블 설정  labels = dict(total_bill ='total_bill($)' ,tip = 'tip($)'
""")

#fig23_
# used df_6
st.markdown("""
---
fig23_scatter_colored_with_unit
""")


#fig23 = px.scatter(df_6, x = 'total_bill', y = 'tip', color = 'sex',
#                 labels = dict(total_bill ='total_bill($)' ,tip = 'tip($)' ) )
#축레이블 설정  labels = dict(total_bill ='total_bill($)' ,tip = 'tip($)'

#fig23.updata_xaxes(title_text = 'total_bill($)')
#fig23.updata_yaxes(title_text = 'tip($)')
#st.plotly_chart(fig23)


#fig24_
st.markdown("""
fig24 Qiz 막대 그래프 그리기
---
    - 주어진 데이터 x = ['A', 'B', 'C', 'D']와 y = [10, 15, 7, 12]를 사용하여 막대 그래프를 그립니다.   
    - 그래프의 가로 크기를 800픽셀, 세로 크기를 600픽셀로 설정하고, 그래프의 제목을 "카테고리별 수치"로 지정합니다.  
---
""")

fig24 = px.bar(x = ['A', 'B', 'C', 'D'], y = [10, 15, 7, 12], title = '카테고리별 수치')
fig24.update_layout(width = 800, height = 600)
st.plotly_chart(fig24)


#fig25
st.markdown("""
---
fig25 
""")

x = ['A', 'B', 'C', 'D']
y = [10, 200, 7, 12]
fig25 = go.Figure(data=go.Bar(x=x,y=y))
fig25.update_layout(
    title = '카테고리별 수치',
    width = 800,
    height = 600
)
st.plotly_chart(fig25)


#fig26
#used df_7
st.markdown("""
---
fig26 
# 축 범위 지정하기

```
fig.update_xaxes(range = [0,10])
fig.update_yaxes(range = [0,10])
```

""")

df_7 = px.data.iris() #붓꽃
df_7
fig26 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' ,color = 'species' )
st.plotly_chart(fig26)
#전체 종 데이터의 혼합표현

#fig27
st.markdown("""
---
### fig27
### facet_col
- 데이터가 좀 더 해석력을 가질 수 있게 해 주는 코드 중에 하나

```
fig = px.scatter(df, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig.show()
```
""")

fig27 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
st.plotly_chart(fig27)

#fig28
st.markdown("""
---
### fig28 facet_col

```
fig.update_xaxes(range = [0,10])
fig.update_yaxes(range = [0,10])
```
""")
fig28 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig28.update_xaxes(range = [0,10])
fig28.update_yaxes(range = [0,10])
st.plotly_chart(fig28)

#fig29
st.markdown("""
---
### fig29 그래프 축 역으로 설정

```
fig.update_yaxes(autorange='reversed')
```
""")
fig29 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig29.update_xaxes(range = [0,10])
fig29.update_yaxes(range = [0,10])
fig29.update_yaxes(autorange='reversed')
st.plotly_chart(fig29)

#fig30
st.markdown("""
---
### fig30  눈금 , tick 레이블 표시 설정

```
fig = px.scatter(df, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig.update_yaxes(ticks='outside')
fig.show()
```
""")
fig30 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig30.update_yaxes(ticks='outside')
st.plotly_chart(fig30)

#fig31
st.markdown("""
---
### fig31  눈금 , tick 레이블 표시 설정

```
fig = px.scatter(df, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig.update_yaxes(ticks='inside')
fig.show()
```
""")
fig31 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig31.update_yaxes(ticks='outside')
st.plotly_chart(fig31)

#fig32


st.markdown("""
---
### fig32  눈금 , tick 레이블 표시 설정

```
fig = px.scatter(df, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig.update_yaxes(ticks='inside' , col = 3)# col = 1,2,3 표현한고 싶은 컬럼에 설정
fig.show()
```
""")
fig32 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig32.update_yaxes(ticks='inside' , col = 3)# col = 1,2,3 표현한고 싶은 컬럼에 설정
st.plotly_chart(fig32)




