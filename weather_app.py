import requests
import streamlit as st
import pandas as pd


def get_weather(city,
                api_key='24a24bc275d34181683b49075212044a',
                units='metric'):
  url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}'
  response = requests.get(url)
  r = response.json()
  # return r
  with open('data.txt', 'w') as file:
    for i in r['list']:
      file.write(
          f"{i['dt_txt']}, {i['main']['temp']}, {i['weather'][0]['description']}\n"
      )
      print(i['dt_txt'], i['main']['temp'], i['weather'][0]['description'])


st.title('Weather Forecast for the Next 5 Days')
place = st.text_input('Place: ')
st.write(f'See the forecast for {place}')
if place:
  get_weather(city=place)
  st.write('The temperature for the next 5 days in', place, 'is:')
  with open('data.txt', 'r') as file:
    for line in file:
      df = pd.read_csv('data.txt', sep=',', header=None)
      df.columns = ['Date', 'Temperature', 'Description']
      st.write(df)

print(get_weather(city='Washington'))
