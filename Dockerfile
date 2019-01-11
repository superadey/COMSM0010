FROM python:alpine3.7
COPY . /app
COPY requirements.txt /app
COPY static /app
COPY templates /app
COPY weather.py /app
RUN apk add
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
