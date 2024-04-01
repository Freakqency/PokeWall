FROM python:latest
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /app
ENV DATA_DIR $DATADIR
ENV USER_TABLE_NAME $USER_TABLE_NAME
ENV API_KEY_LENGTH $API_KEY_LENGTH
EXPOSE "8000"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#TODO: Persist data folder in docker
