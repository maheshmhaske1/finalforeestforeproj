import streamlit as st
import pandas as pd
import numpy as np
#import weather
import requests
import time
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



data_complete=pd.read_csv('Forest_fire.csv')
data_head=data_complete.head()
data_tail=data_complete.tail()
a=st.sidebar.radio('navigation',['show database','show visualization','MANUAL ML MODULE','AUTOMATED ML MODULE'])


y0 = np.array(data_complete['Fire Occurrence']).reshape(-1,1)
x0= np.array(data_complete['Temperature']).reshape(-1,1)
x=data_complete.drop(data_complete.columns[[0,4]],axis=1)
y=data_complete.drop(data_complete.columns[[0,1,2,3]],axis=1)
lr=LinearRegression()
lr.fit(x,y)

if a=='show database':

    if st.checkbox("complete database"):
        st.text("showing complete database")
        data_complete
        st.balloons()


    elif st.checkbox('show head of database'):
        st.text("showing head of database")
        data_head
        st.balloons()

    elif st.checkbox('show tail of database'):
        st.text("showing tail if database")
        data_tail
        st.balloons()
    




elif a=='show visualization':
    if st.checkbox("BAR CHART"):
        st.bar_chart(data_complete['Oxygen'])
        st.bar_chart(data_complete['Temperature'])
        st.bar_chart(data_complete['Humidity'])

       
    elif st.checkbox('LINE CHART'):
        st.line_chart(data_complete)


    elif st.checkbox('COMPLETE BAR CHART'):
        st.bar_chart(data_complete)



elif a=='MANUAL ML MODULE':
    oxygen1=st.number_input('oxygen')
    temp1=st.number_input('temrature')
    humidity1=st.number_input('humdity')
    model=LinearRegression()
    if st.button('predict'):
        progress=st.progress(0)
        for i in range(100):
            time.sleep(0.001)
            progress.progress(i+1)
        model.fit(x,y)
        op=(model.predict([[oxygen1,temp1,humidity1]]))
        st.text('RESULT : ')
        op
        if op >0.50:
            st.warning('forrest in danger')
        else:
            st.success('forrest in safe')
            st.balloons()
    r=st.radio('view data',['input','outout'])
    if r=='input':
        x
    elif r=='outout':
        y
  
elif a=='AUTOMATED ML MODULE':

    user_input = st.text_input("ENTER CITY", 'pune')
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ac4073a87a991a712b197b7e8bc04930&units=metric'.format(user_input)
    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    humidity = data['main']['temp']
    wind_speed = data['wind']['speed']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    description = data['weather'][0]['description']
    if st.button('predict'):
        model1=LinearRegression()
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.001)
            progress.progress(i + 1)
        model1.fit(x, y)
        op = (model1.predict([[2, temp,humidity]]))
        st.text('RESULT : ')
        op
        if op > 0.50:
            st.warning('forrest in danger')
        else:
            st.success('forrest in safe')
        st.text(data)
        

