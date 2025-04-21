# import streamlit as st
# import random
# from streamlit_elements import elements, mui, html
# st.title("Marriage Prediction")

# with st.form("Marriage_Form"):
#     # name with placeholder

#     your_name = st.text_input("Your Name",placeholder="Enter your name") 
#     partner_name = st.text_input("Partner Name",placeholder="Enter your partner name")
#     # date of birth with placeholder
#     your_dob = st.date_input("Your Date of Birth")
#     partner_dob = st.date_input("Partner Date of Birth")
#     # location with placeholder
#     your_location = st.text_input("Your Location",placeholder="Enter your location")
#     partner_location = st.text_input("Partner Location",placeholder="Enter your partner location")    
#     # Dropdown for zodiac signs
#     your_zodiac = st.selectbox("Your Zodiac Sign", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
#     partner_zodiac = st.selectbox("Partner Zodiac Sign", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
#     # Submit button
    
#     submitted = st.form_submit_button("Predict")
# # onclick
# if submitted:
#     st.write("You clicked the button")
#     st.write("Your Name:", your_name)
#     st.write("Partner Name:", partner_name)
#     st.write("Your chances of marriage are:", random.randint(0, 100), "%")

# st.write("Share your results with your friends!")
# with elements("multiple_childrens"):
#     mui.Button(
       
#         mui.icon.Facebook(),
#         mui.icon.Twitter(),
#         mui.icon.Instagram(),


#     )

import streamlit as st
import random
import requests
from streamlit_elements import elements, mui

st.title("Marriage Prediction")

with st.form("Marriage_Form"):
    your_name = st.text_input("Your Name", placeholder="Enter your name")
    partner_name = st.text_input("Partner Name", placeholder="Enter your partner name")
    your_dob = st.date_input("Your Date of Birth")
    partner_dob = st.date_input("Partner Date of Birth")
    your_location = st.text_input("Your Location", placeholder="Enter your location")
    partner_location = st.text_input("Partner Location", placeholder="Enter your partner location")
    your_zodiac = st.selectbox("Your Zodiac Sign", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    partner_zodiac = st.selectbox("Partner Zodiac Sign", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    
    submitted = st.form_submit_button("Predict")

if submitted:
    match_percent = random.randint(0, 100)
    
    st.success("Your prediction was submitted successfully!")
    st.write("Your Name:", your_name)
    st.write("Partner Name:", partner_name)
    st.write("Your chances of marriage are:", match_percent, "%")

    # Xano API POST request
    xano_url = "Enter your Xano API URL here"  # Replace with your Xano API URL  
    payload = {
        "your_name": your_name,
        "partner_name": partner_name,
        "your_dob": str(your_dob),
        "partner_dob": str(partner_dob),
        "your_location": your_location,
        "partner_location": partner_location,
        "your_zodiac": your_zodiac,
        "partner_zodiac": partner_zodiac,
        "match_percent": match_percent
    }

    response = requests.post(xano_url, json=payload)

    if response.status_code == 200 or response.status_code == 201:
        st.success("Saved to database!")
    else:
        st.error("Error saving data to Xano.")

st.write("Share your results with your friends!")

with elements("multiple_childrens"):
    mui.Button(mui.icon.Facebook())
    mui.Button(mui.icon.Twitter())
    mui.Button(mui.icon.Instagram())
