FROM python:3-slim-stretch

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9132

CMD [ "python", "app.py" ]