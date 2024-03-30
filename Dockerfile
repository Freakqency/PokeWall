FROM python:latest
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /app
EXPOSE "8000"
# ENV DATA_DIR="./data"
# ENV USER_TABLE_NAME="users"
# ENV API_KEY_LENGTH="16"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#TODO: Persist data folder in docker