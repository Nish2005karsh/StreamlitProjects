# import streamlit_scrollable_textbox as stx
# import streamlit_scrollable_textbox as stx
from streamlit_elements import elements, mui, html
import streamlit as st



st.title('My Portfolio')


st.subheader('Hello, I am Kevin Rush')
st.image("KevinRushProfile.jpg", width=200)


st.write("""
    I am a passionate web developer, specializing in Python, JavaScript, and web development frameworks.
    I have experience building full-stack web applications and am eager to continue learning and growing in the field.
    Here are some of my projects and skills!
""")


st.subheader('Skills')
st.write("""
- Python
- JavaScript
- HTML, CSS
- React
- Streamlit
- Node.js
""")


st.subheader('Projects')


st.write("Check out my projects below:")


st.write("[Project 1: My Web App](https://link-to-project-1.com)")
st.write("[Project 2: Portfolio Site](https://link-to-project-2.com)")
st.write("[Project 3: AI-based Chatbot](https://link-to-project-3.com)")


st.subheader('Contact')
st.write("""
You can reach me at:
- Email: [your-email@example.com](mailto:your-email@example.com)
""")

name=st.text_input("Name")
email=st.text_input("Email")
message=st.text_area("Message")
if st.button("Submit"):
    st.write("Thank you for your message!")
    st.write(f"Thanks for reaching out, {name}!")
    st.write(f"We will get back to you at {email} as soon as possible.")
    st.write("Your message:")
    st.write(message)
st.write("You can also find me on social media:")
st.markdown("[LinkedIn](https://www.linkedin.com/in/yourprofile)")
st.markdown("[GitHub](URL_ADDRESS.com/yourusername)")
with elements("multiple_childrens"):
    mui.Button(
        mui.icon.Instagram(),
        mui.icon.Facebook(),
        mui.icon.Twitter(),
        mui.icon.LinkedIn()
        
    )






    