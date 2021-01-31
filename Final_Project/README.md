# **Assignment 3**

## Team Information

| Name | NEU ID 
| --- | --- 
|Prathamesh Shrikrishna Verlekar | 001376578 
|Yash Pandya | 001346162

## Dataset Kaggle link

Colab link

https://codelabs-preview.appspot.com/?file_id=1wwoLIavhAn-CVJkaIrQI8Lx4-xSZeWoGJ2dCHv4-aTQ/edit#0

## Alibaba Digital Marketing

![alibaba (1)](https://user-images.githubusercontent.com/55213702/90303714-4c906b00-de7e-11ea-818a-7a249c0f4d33.jpg)

## About Alibaba

Alibaba Group Holding Limited (also known as Alibaba Group and Alibaba.com) is a Chinese multinational technology company specializing in e-commerce, retail, Internet, and technology. 
On 19th September 2014, Alibaba's market value was US$231 billion. It is one of the top 10 most valuable and is the 59th biggest public company in the world by the Global 2000 list.

## Goals of the Project

-> Finding Recency, Frequency, and Monetary Value to find the company's best customers by using certain measures.\
-> Build a recommendation system for suggesting products to the customers that they might also like.\
-> To Crawl, Index, and Rank data using the Search engine for better customer experience.\
-> Build a dashboard for business owners to better understand their sales and decide future marketing strategies.\
-> Create a web application for better user experience.

## About Dataset used for the project

-> We will be using datasets available on Kaggle along with data available through different open sources and websites.\
-> Kaggle Dataset  Link:https://www.kaggle.com/AppleEcomerceInfo/ecommerce-information?select=products.txt \
-> http://yongfeng.me/dataset/  

## Personas

Who – Alibaba’s technical teams, stakeholders, and sponsors for deciding their future marketing strategies.
 
What – Build a recommendation system for the company’s customers and dashboards for stakeholders to analyze their sales and other insights.
 
When – It will be completed within 2 weeks of a given timeline.
 
Where – We will be working at our remote locations and then collaborate on our work.
 
Why – To get data insights that will help the stakeholders decide their marketing strategies and to improve the customer experience by building a recommendation system that will recommend the customers product that may also like.
 
How – Using the tools and technologies learned in the course.

## Workflow

![Capture](https://user-images.githubusercontent.com/55213702/90303816-5a92bb80-de7f-11ea-8ec8-5d62eb25eb88.PNG)

## Web Scraping

Web Scraping (also termed Screen Scraping, Web Data Extraction, Web Harvesting, etc.) is a technique employed to extract large amounts of data from websites whereby the data is extracted and saved to a local file in your computer or to a database in table (spreadsheet) format.

![Capture2](https://user-images.githubusercontent.com/55213702/90303836-a8a7bf00-de7f-11ea-897b-878503eaa483.PNG)

## Trifacta

Trifacta's data wrangling software allows you to prepare & visualize complex data in no time.

![Capture3](https://user-images.githubusercontent.com/55213702/90303854-e278c580-de7f-11ea-9ac4-ef0f94d36ebc.PNG)

## RFM and Customer Segmentation

RFM stands for three dimensions:
Recency – How recently did the customer purchase?
Frequency – How often do they purchase?
Monetary Value – How much do they spend?

We have calculated the RFM values for each customers and based on that we have calculated the RFMScore, using which we have segmented customers into different categories.

![Capture4](https://user-images.githubusercontent.com/55213702/90303907-68950c00-de80-11ea-8da0-6ff781535006.PNG)

## Snowflake

Snowflake is a cloud-based Data Warehouse solution provided as a Saas (Software-as-a-Service) with full support for ANSI SQL. It also has a unique architecture that enables users to just create tables and start querying data with very little administration or DBA activities needed.

We created tables in snowflake to store our data which we connected to Salesforce Einstein Analytics for building dashbaords.

## Salesforce Einstein Analytics Dashboard

Salesforce.com, inc. is an American cloud-based software company headquartered in San Francisco, California. It provides customer relationship management (CRM) service and also sells a complementary suite of enterprise applications focused on customer service, marketing automation, analytics, and application development.

Using Salesforce we calculated mentioned insights,

-> Total Revenue generated , Total Quantity sold, Top country that use the website\
-> Which Country has purchased most items\
-> Category wise items ordered and Cancelled\
-> How many items after placing in cart where purchased\
-> Number of orders based on weekdays\
-> Which has platform(Phone and Web) used for Most\
-> Quantity sold based on segments (Loyal, potential Loyalist, Cannot lose them, new Customer and Lost customers)\
-> Tablewise segmentation

## Dashboard for Alibaba Insights

![WhatsApp Image 2020-08-14 at 10 51 52 PM](https://user-images.githubusercontent.com/55213702/90303961-eb1dcb80-de80-11ea-9681-ff5b45f6a37b.jpeg)

## Recommendation Models

LightGCN is a simplified design of GCN to make it more concise and appropriate for a recommendation.

![Capture5](https://user-images.githubusercontent.com/55213702/90304002-5d8eab80-de81-11ea-8dcc-fdd06703169f.PNG)

Surprise Singular Value Decomposition (SVD)

SVD introduces two new scalar variables: the user biases bu and item biases bi. The user biases are supposed to capture the tendency of some users to rate items higher (or lower) than the average.

## Search Engine

One typical business case is an eCommerce website that allows to search of a poster based on the example uploaded by the user. A user would usually expect to get results that are similar in terms of artistic style.

![Capture6](https://user-images.githubusercontent.com/55213702/90304028-a8102800-de81-11ea-8326-9098b9e8671a.PNG)

## Streamlit Application 

Streamlit is an open-source app framework for Machine Learning and Data Science teams. Create beautiful data apps in hours, not weeks. All in pure Python.

https://finalproject-streamlit-app.herokuapp.com/

![Capture7](https://user-images.githubusercontent.com/55213702/90304061-e279c500-de81-11ea-98d3-b3dc02eeef31.PNG)

## Heroku Deployment

Heroku is a cloud platform as a service supporting several programming languages. One of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go.

We deployed our streamlit Application on Heroku.

![Capture8](https://user-images.githubusercontent.com/55213702/90304103-1f45bc00-de82-11ea-8354-df4ec4439ab5.PNG)

## FastAPI

We connected our recommendation model to FastAPI and used in Flask for showing recommendations to customers.

![Capture9](https://user-images.githubusercontent.com/55213702/90304129-6f248300-de82-11ea-9a9e-a82f5f2de3e0.PNG)

## Flask Application deployed on AWS

http://ec2-3-83-205-192.compute-1.amazonaws.com:5000/home.html

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

AWS provides on-demand access to scalable web and application servers, storage, databases, content delivery, cache, search, and other application services that make it easier to build and run apps that deliver a great customer experience.

![Capture10](https://user-images.githubusercontent.com/55213702/90304166-c1fe3a80-de82-11ea-8e0c-d85687a81de7.PNG)

![Capture](https://user-images.githubusercontent.com/55213702/90304216-56689d00-de83-11ea-94ee-8b37887f02b9.PNG)

![Capture0](https://user-images.githubusercontent.com/55213702/90304215-55d00680-de83-11ea-91e4-7ee46f82dcbc.PNG)

## References

-> https://github.com/microsoft/recommenders \
-> https://fastapi.tiangolo.com/tutorial/body/ \
-> https://github.com/microsoft/recommenders/blob/master/examples/00_quick_start/sequential_recsys_amazondataset.ipynb \
-> https://github.com/microsoft/recommenders/blob/master/examples/02_model_collaborative_filtering/lightgcn_deep_dive.ipynb \
-> https://github.com/microsoft/recommenders/tree/master/tests \
-> https://github.com/davidefiocco/streamlit-fastapi-model-serving







