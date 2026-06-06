import streamlit as st 
import requests
base_url="http://127.0.0.1:8000"
st.title("🌤️ AI Weather Forecaster")
city=st.text_input("Enter City")
question=st.text_input("Ask Your Weather Question")


if st.button("ASK AGENT"):
    res=requests.post(f"{base_url}/get_weather",params={
                      
                      "city":city,
                      "question":question
                      
                      })
  
    data = res.json()
    # st.write(data)  
    st.success(data["messages"][-1]["content"])
   
  
    


