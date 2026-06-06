import streamlit as st 
import requests
base_url="https://ai-weather-forecaster-1.onrender.com"
st.title("🌤️ AI Weather Forecaster")
city=st.text_input("Enter City")
question=st.text_input("Ask Your Weather Question")


if st.button("ASK AGENT"):
    res=requests.post(f"{base_url}/get_weather",params={
                      
                      "city":city,
                      "question":question
                      
                      })
    st.write(res.status_code)
    st.write(res.text)
    # data = res.json()
    # st.success(data["messages"][-1]["content"])
   
  
    



