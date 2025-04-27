import streamlit as st
import requests
st.title('🌦️ Weather App')
city = st.text_input('Enter a city name')
if city:
    api_key = 'Enter the api ley of open weather map'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get('cod') == 200:
        st.subheader(f"Weather in {city}")
        st.write(f"🌡️ Temperature: {data['main']['temp']} °C")
        st.write(f"🧥 Feels Like: {data['main']['feels_like']} °C")
        st.write(f"💧 Humidity: {data['main']['humidity']}%")
        st.write(f"🌬️ Wind Speed: {data['wind']['speed']} m/s")
        st.write(f"☁️ Weather Description: {data['weather'][0]['description'].capitalize()}")
        st.write(f"🌅 Sunrise: {data['sys']['sunrise']}")
        st.write(f"🌇 Sunset: {data['sys']['sunset']}")
        
        st.image(f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png")
        


    else:
        st.error("City not found. Please check the name.")
