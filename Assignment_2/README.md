# **Assignment 2**

## Team Information

| Name | NEU ID 
| --- | --- 
|Prathamesh Shrikrishna Verlekar | 001376578 
|Yash Pandya | 001346162

## Dataset Kaggle link

Colab link

https://codelabs-preview.appspot.com/?file_id=1w6cRM7R4vR45zwsY5jq2GiY2LWJSNCDkoq2zAToK6GA/edit#0


## About Dataset

It has almost 9 million products: half of the current catalogue
More than 15 million images at 180x180 resolution
More than 5000 categories: yes this is quite an extreme multi-class classification!

## Kaggle Link: https://www.kaggle.com/c/cdiscount-image-classification-challenge

train.bson :
(Size: 58.2 GB) Contains a list of 7,069,896 dictionaries, one per product. Each dictionary contains a product id (key: _id), the category id of the product (key: category_id), and between 1-4 images, stored in a list (key: imgs). Each image list contains a single dictionary per image, which uses the format: {'picture': b'...binary string...'}. The binary string corresponds to a binary representation of the image in JPEG format. This kernel provides an example of how to process the data.

category_names.csv:
Shows the hierarchy of product classification. Each category_id has a corresponding level1, level2, and level3 name, in French. The category_id corresponds to the category tree down to its lowest level. This hierarchical data may be useful, but it is not necessary for building models and making predictions. All the absolutely necessary information is found in train.bson.

train_example.bson:
Contains the first 100 records of train.bson so you can start exploring the data before downloading the entire set.

## Algorithms used in the project

## Cosine Similarity Algorithm
Cosine similarity is the cosine of the angle between two n-dimensional vectors in an n-dimensional space. It is the dot product of the two vectors divided by the product of the two vectors' lengths (or magnitudes).

## Facebook AI Similarity Search using FAISS
Facebook AI Similarity Search (Faiss), a library that allows us to quickly search for multimedia documents that are similar to each other — a challenge where traditional query search engines fall short.

So, for similarity search and classification, we need the following operations:

Given a query vector, return the list of database objects that are nearest to this vector in terms of Euclidean distance.
Given a query vector, return the list of database objects that have the highest dot product with this vector.

With Faiss, we introduce a library that addresses the limitations mentioned above. Among its advantages:

Faiss provides several similarity search methods that span a wide spectrum of usage trade-offs.
Faiss is optimized for memory usage and speed.
Faiss offers a state-of-the-art GPU implementation for the most relevant indexing methods.

## Spotify Annoy Method

Annoy (Approximate Nearest Neighbor Oh Yeah), is an open-sourced library for finding approximate nearest neighbors. This algorithm builds an annoy index by appending all image feature vectors stored in the local folder. The annoy library is basically used to solve the problem of Nearest Neightbour search (NNS) for the Euclidean distance, Manhattan distance, cosine distance, Hamming distance, or Dot (Inner) Product distance. With Annoy, you will build a net of dots or vectors in a n dimensional space, in order to then ask it to give you different propierties of this given net. One of the advantatges in using this library is that it is specially efficient when it comes to memory storage.


## Application Screenshots

![Second_SS](https://user-images.githubusercontent.com/55213702/89846680-dcb57400-db4f-11ea-8bd5-7b66c8431ff8.jpeg)

![Flask_AWS (2)](https://user-images.githubusercontent.com/55213702/89846654-cad3d100-db4f-11ea-9990-46426b927564.jpeg)

