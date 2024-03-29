FROM python:latest
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /app
EXPOSE "8000"
CMD ["sh", "/app/startup.sh"]

#TODO: Persist data folder in docker
#TODO: Deploy to azure