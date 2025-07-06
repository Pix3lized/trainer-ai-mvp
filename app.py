# How to run this app:
# export GROQ_API_KEY=<your_groq_api_key>
# streamlit run app.py

import streamlit as st
from groq_client import get_llm_response

st.title("TrainerAI")
st.write("Enter your fitness goal, eating habits, health conditions, and lifestyle to get a personalized diet and training plan.")

user_input = st.text_area("Your Input", height=100)
if st.button("Get Plan"):
    if user_input:
        with st.spinner("Generating your personalized plan..."):
            response = get_llm_response(user_input)
        st.write("### Your Personalized Plan:")
        st.write(response)
    else:
        st.error("Please enter your fitness goal, eating habits, health conditions, and lifestyle.")

st.sidebar.header("About")
st.sidebar.write("TrainerAI is an AI-powered fitness coach that provides personalized diet and training plans.")
