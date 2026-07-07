
import streamlit as st 
import requests
# BASE_URL="http://127.0.0.1:8000"
BASE_URL="https://ai-weather-forecaster-4.onrender.com"
st.title("🌤️ AI Weather Forecaster")
city=st.text_input("Enter City")
question=st.text_input("Ask Your Weather Question")


if st.button("Ask Agent"):
    res=requests.post(f"{BASE_URL}/get_weather",params={
        "city":city,
        "question":question
    })
    
   
    st.write("STATUS:", res.status_code)
    st.success(res.json()["messages"][-1]["content"]) 
    
    
    
    
     


  
    
    
    
    
     
