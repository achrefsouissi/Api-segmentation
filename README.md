# MobileSam Segmentation Model Service

## Overview
This project provides a FastAPI service to deploy the MobileSam segmentation model. The service allows users to interact with the model via a RESTful API, processing image inputs and returning segmentation results. Additionally, the service can be containerized using Docker for easy deployment.

## Setup

### Requirements
- Python 3.9
- Docker (optional, for containerization)

### Installation
1. Clone the repository:
   git https://github.com/achrefsouissi/Api-segmentation
   cd Api-Mobilesam-Task-Stage
### Note: The API is located in the 'Api-Mobilesam-task-stage' folder.
   
# Running the Service - Without Docker - Run the FastAPI service:

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
-> The service will be accessible at http://localhost:8000.
-> Open your browser or API testing tool (e.g., Postman).

Use the /segment-image endpoint to process images and obtain segmentation results.

## With Docker (Optional) - Build the Docker image:
docker build -t mobilesam-segmentation-service .
## Run the Docker container:
docker run -p 8000:8000 mobilesam-segmentation-service
The service will be accessible at http://localhost:8000.
Open your browser or API testing tool.

Use the /segment-image endpoint to process images and obtain segmentation results.

#### Interacting with the API
Endpoint: /segment-image
Method: POST
Description: Accepts an image file, processes it through MobileSam, and returns the segmentation result.

1. open 127.0.0.1/docs
2. test the api with POST METHOD 

####Notes : 
The service is configured to run on CPU by default. If GPU support is available, adjust the device settings in segmentation.py.



