# # Practicing streamlit.py
# # This is a practice file for streamlit.py
# import streamlit as st
# import pandas as pd
# st.title("Hello WOorld!")
# st.write("This is a practice file for streamlit.py")
# # Lets do pandas with streamlit
# st.write("Lets do pandas with streamlit")
# st.write("This is a practice file for streamlit.py")
# with st.form("Normal_Form"):
#     date = st.date_input("Date")
#     category = st.selectbox("Hobbies", ["Food", "Travel", "Shopping", "Bills", "Other"])
#     amount = st.number_input("Amount", min_value=0.0, step=0.01)
#     submitted = st.form_submit_button("Add Expense")

# st.sidebar.title("Sidebar")
# st.sidebar.write("This is a sidebar")
# # Onclick
# st.sidebar.button("Click me")
# st.sidebar.write("You clicked the button")
# st.chat_message("W")
# st.chat_message("This is a chat message")
# but=st.checkbox("This is a checkbox")
# if but:
#     st.write("You clicked the checkbox")
# else:
#     st.write("You did not click the checkbox")
# # Radio button
# k=st.radio("This is a radio button", ["Yes", "No"])
# if k=="Yes":
#     with st.form("Radio_Form"):
#         date = st.date_input("Date")
#         submitted=st.form_submit_button()
#         if submitted:
#             st.write("You clicked the radio button")

# else:
#     st.write("You did not click the radio button")

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# with st.form("Normal_Form"):
#     date = st.date_input("Date")
#     category = st.selectbox("Hobbies", ["Food", "Travel", "Shopping", "Bills", "Other"])
#     submitted=st.form_submit_button("Add Expense")
#     if submitted:
#         st.write("You clicked the button")
#         st.write("Date:", date)
#         st.write("Category:", category)
#     else:
#         st.write("You did not click the button")
# Using matplotlib with streamlit
# Create a simple plot
# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np
# # Generate some random data
# x=np.linspace(0, 10, 100)
# y=np.sin(x)
# # Create a plot
# fig, ax=plt.subplots()
# ax.plot(x, y)
# st.write("Plot")
# st.pyplot(fig)
# # Create a histogram
# data=np.random.randn(1000)
# fig, ax=plt.subplots()
# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np
# Create a element with a child
from streamlit_elements import elements,mui,html
with elements("new_element"):
    mui.Typography("Hello World", variant="h2")
with elements("multiple_childrens"):
    mui.Button(
        mui.icon.EmojiPeople(),
        mui.icon.Facebook(),
        
    )
    with mui.Paper:
        with mui.Typography:
            html.p("Hello world")
            html.p("Goodbye world")
            html.br()




