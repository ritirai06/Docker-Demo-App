#base image
FROM python:3.9-slim
#workdir
WORKDIR /app    
#copy files
COPY . /app
#install dependencies
RUN pip install -r requirements.txt 
#port
EXPOSE 5000
#cmd
CMD ["python", "app.py"]