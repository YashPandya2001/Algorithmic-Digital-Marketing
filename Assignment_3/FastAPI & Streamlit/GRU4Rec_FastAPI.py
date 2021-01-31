import uvicorn
from fastapi import FastAPI,Query
import joblib

# Models
rlrmc = open("GRU4Rec.SAV","rb")
rlrmc_model = joblib.load(rlrmc)

# init app
app = FastAPI()

# Routes
@app.get('/')
async def index():
	return {"text":"Hello API Masters"}

@app.get('/user/{user_id}')
async def get_users(user_id:int):
	return {"user_id":user_id}

@app.get('/product/{product_id}')
async def get_products(product_id:int):
	return {"product_id":product_id}

# ML Aspect
""" @app.get('/predict/user_id={user_id}&product_id={product_id}')
async def predict(user_id:int, product_id:int):
	user_list = []
	prod_list = []
	user_list.append(user_id)
	prod_list.append(product_id)
	prediction = rlrmc_model.predict(user_list, prod_list)
	if prediction[0] > 0:
		result = prediction[0]
	else:
		result = "Not Found"

	return {"prediction":result} """

@app.get('/predict/')
async def predict(user_id:int = 1, product_id:int = 65):
	user_list = []
	prod_list = []
	user_list.append(user_id)
	prod_list.append(product_id)
	prediction = rlrmc_model.predict(user_list, prod_list)
	if prediction[0] > 0:
		result = prediction[0]
	else:
		result = "Not Found"

	return {"prediction":result} 



if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)
