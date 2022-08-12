import streamlit as st
import pandas as pd
import datetime as dt
import yfinance as yf
import plotly.graph_objs as go
import plotly.express as px
import matplotlib.pyplot as plt
from model import prediction

st.title(""" Stock Predictor...
""")
st.image("stock.jpg")
st.write("Input Stock Code")
stock_name = st.text_input("")
model = yf.Ticker(stock_name)
# st.write(model.history(period="max"))
x=model.info
df=model.history(period="max")
try:
    st.write(x["longBusinessSummary"])
except:
    st.text("Which Stock to predict !!!")

# st.date_input("Start Date -")
# st.text(f"End Date - {dt.date.today()}")

def Button_Graph(df):
    df = pd.DataFrame(df,columns=["Open","Close"])
    st.line_chart(df)

def get_more(df):
    df['EWA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df = pd.DataFrame(df,columns=["EWA_20"])
    st.line_chart(df) 

if st.button("Stock Price"):
    Button_Graph(df)

if st.button("Indicators"):
    get_more(df)
   
num_days = st.number_input("No of Days",min_value=1,max_value=50,step=1)
if st.button("Forecast"):
    prediction(stock=stock_name,n_days=num_days)
