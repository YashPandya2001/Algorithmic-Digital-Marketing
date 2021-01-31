import uvicorn
from fastapi import FastAPI,Query
import joblib
import csv
import pandas as pd

# init app
app = FastAPI()

# Routes
@app.get('/')
async def index():
    return {"text":"Hello API Masters"}

@app.get('/items/{user_id}')
async def get_items(user_id:int):
    return {"user_id":user_id}

@app.get('/items/{product_id}')
async def get_items(product_id:int):
    return {"product_id":product_id}

# ML Aspect
@app.get('/lightGCN/')
async def predict(user_id:int=1, snack_id:int=65):
    
    dataframe = pd.read_csv("LightGCN.csv")
    prediction = dataframe.loc[(dataframe['userID'] == user_id) & (dataframe['snackID'] == snack_id), ['prediction']]

    return {"prediction":prediction}

if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)
