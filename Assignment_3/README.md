# **Assignment 3**

## Team Information

| Name | NEU ID 
| --- | --- 
|Prathamesh Shrikrishna Verlekar | 001376578 
|Yash Pandya | 001346162

## Dataset Kaggle link

Colab link

https://codelabs-preview.appspot.com/?file_id=1FtH6NZWavwhMyeGttyGZ0Q3aVrlgi8FrrKnPgXnAEfQ/edit#0

## About Recommendation Systems

Recommendation algorithms play a crucial role in fast searching on a website for a user. A Company is a large e-tailer who has millions of products in catalog. They intend to enhance the user-experience of their client by providing them with a rich and engaging interface.

## Dataset 

We generated fake dataset using Faker library available in Python.

![Capture1](https://user-images.githubusercontent.com/55213702/90304727-97af7b80-de88-11ea-83a5-bc44c8a76a35.PNG)

## Recommendation Models

We used two recommendation models.

Sequential Recommender (GRU4Rec) and Light GCN model for building our system.

![Capture3](https://user-images.githubusercontent.com/55213702/90304802-5370ab00-de89-11ea-9521-a4933abb1d0c.PNG)

![Capture2](https://user-images.githubusercontent.com/55213702/90304803-5370ab00-de89-11ea-8ebd-000a4ba078b4.PNG)

## FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

![Capture4](https://user-images.githubusercontent.com/55213702/90304827-ac404380-de89-11ea-9a55-25e4a962c8cc.PNG)

## Apache Jmeter

Apache J meter is java open source software that is used as a load testing tool for analyzing and measuring the performance of a variety of services. It was first developed by Stefano Mazzocchi of the Apache Software Foundation, designed to load test functional behavior and measure performance.

![Capture5](https://user-images.githubusercontent.com/55213702/90304862-09d49000-de8a-11ea-86e8-1cade6322ae9.PNG)

## Streamlit Application

We connected our recommendation models to streamlit application with the help of FastAPI.

1. Streamlit apps are Python scripts that run from top to bottom.
2. Every time a user opens a browser tab pointing to your app, the script is re-executed.
3. As the script executes, Streamlit draws its output live in a browser.
4. Scripts use the Streamlit cache to avoid recomputing expensive functions, so updates happen very fast.
5. Every time a user interacts with a widget, your script is re-executed and the output value of that widget is set to the new value during that run.

![Capture6](https://user-images.githubusercontent.com/55213702/90304965-3dfc8080-de8b-11ea-8f12-c8282ac93381.PNG)

## References

https://github.com/microsoft/recommenders \
https://fastapi.tiangolo.com/tutorial/body/ \
https://github.com/microsoft/recommenders/blob/master/examples/00_quick_start/sequential_recsys_amazondataset.ipynb \
https://github.com/microsoft/recommenders/blob/master/examples/02_model_collaborative_filtering/lightgcn_deep_dive.ipynb \
https://github.com/microsoft/recommenders/tree/master/tests \
https://github.com/davidefiocco/streamlit-fastapi-model-serving






