from fastapi import FastAPI,Query
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain.tools import tool
import os
from dotenv import load_dotenv 
import requests

load_dotenv()    
    
app=FastAPI()
OPENWEATHER_API_KEY=os.getenv("OPENWEATHER_API_KEY")

llm=ChatGroq(
    
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")

)

@tool
def get_temperature_details(city:str):
    """
    Get real-time weather information for a city using OpenWeatherMap.
    Use this tool whenever the user asks about temperature,
    weather conditions, humidity, wind speed, clouds, rain,
    forecast, or any weather-related question.
    """
    res=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric")
    print("Status Code:", res.status_code)
    print("Response:", res.json())
    return res.json()

agent=create_agent(
    
    model=llm,
    tools=[get_temperature_details]
)

@app.post("/get_weather")
def incoming_weather_params(
    city: str=Query(...),
    question: str=Query(...)
    ):
    result=agent.invoke({
        "messages":[{
            "role":"user",     
            "content": f"""
            You are a friendly Weather AI Assistant.
            Always use the get_temperature_details tool to get real-time weather information before answering.
            User City: {city}
            User Question: {question}
            Provide:
            1. Current temperature in °C
            2. Weather condition
            3. Humidity
            4. Wind speed
            5. A short friendly summary
            Do not make up weather information.
            Only use data returned by the tool.
            """      
    }]
            })
    print(result)
    return result

            
    






    
