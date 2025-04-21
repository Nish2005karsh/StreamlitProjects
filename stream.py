import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
if 'data' not in st.session_state:
    st.session_state['data'] = pd.DataFrame(columns=["Date", "Category", "Amount"])

st.title("💸 Personal Expense Tracker")


with st.form("expense_form"):
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        new_entry = {"Date": date, "Category": category, "Amount": amount}
        st.session_state['data'] = pd.concat([st.session_state['data'], pd.DataFrame([new_entry])], ignore_index=True)
        st.success("Expense added!")

st.subheader("📊 Expense History")
st.dataframe(st.session_state['data'])
if not st.session_state['data'].empty:
    st.subheader("📈 Expense Breakdown by Category")
    category_totals = st.session_state['data'].groupby("Category")["Amount"].sum()
    
    fig, ax = plt.subplots()
    category_totals.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_ylabel("")  
    ax.set_title("Spending Distribution")
    st.pyplot(fig)


