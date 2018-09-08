 #Pull base image
 FROM python:3.6-slim
 
 #Set environment variables	
 ENV PYTHONUNBUFFERED 1
 
 #Set working directory
 RUN mkdir /code
 WORKDIR /code
  	
 #Install dependencies
 COPY requirements.txt /code/
 RUN pip install -r requirements.txt
 

 #Copy prokect
 COPY . /code/
