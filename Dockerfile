FROM python:3.11-alpine

ADD * ./

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]
