import streamlit as st
#from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
from PIL import Image
import io
import joblib
from abcd import predict
import pandas as pd


st.title('Microsoft Recommendation Algorithms for SNACKS')
image = Image.open('snack.jpg')

st.image(image,use_column_width=True)

st.markdown('<style>body{background-color: #FF5733;}</style>',unsafe_allow_html=True)
st.markdown('*ALGORITHMS FOR SNACKS SELECTION*')

# Models
rlrmc = open("GRU4Rec.SAV","rb")
rlrmc_model = joblib.load(rlrmc)
url = 'http://127.0.0.1:8000/'
endpoint = 'predict/'

def get_data(user_id,pro_id):
    server_url = url + endpoint + str(user_id) + ',' + str(pro_id)
    r= requests.get(server_url)
    return r.json()

radio = st.radio(
    "Choose an algorithm-->",
    ("GRU4Rec Algorithm","LightGCN Algorithm"))

if radio == 'LightGCN Algorithm':
    
    title = st.number_input('User ID',min_value = 0,max_value=1000,value = 0,step =1)
    
    
    data = pd.read_csv('LightGCN.csv')
    df1 =  data['userID']==title
    df2 = data[df1]
    data = pd.DataFrame(df2.iloc[:,1:4])

    st.dataframe(data)
    

if radio == 'GRU4Rec Algorithm':
    
    title = st.number_input('User ID',min_value = 0,max_value=1000,value = 0,step =1)
    
    
    data = pd.read_csv('GRU4Rec.csv')
    df1 =  data['userID']==title
    df2 = data[df1]
    data = pd.DataFrame(df2.iloc[:,1:4])

    st.dataframe(data)
    
#image = Image.open('snack.jfif')

#st.image(image, caption='Snack Recommendation',use_column_width=True)


