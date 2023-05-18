FROM alpine:3.14
RUN apk add --update py-pip
RUN pip install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 6001
CMD ["python3", "app.py"]
