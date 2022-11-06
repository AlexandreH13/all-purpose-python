# Dockerfile: Blueprint for images 
# Images: Templates to run the containers
# Container: The process used to run the application
# Running locally specifying the ports mapping: docker run -p 8000:8000 container_name

FROM python:3.8

# create a work directory inside the container
WORKDIR /fastapi-app

# copy the requirements inside the workdir
COPY requirements.txt .

# install the requirements
RUN pip install -r requirements.txt

# copy the app folder to workdir
COPY ./app ./app

# Specify the entry command when run the container
CMD ["python", "./app/main.py"]