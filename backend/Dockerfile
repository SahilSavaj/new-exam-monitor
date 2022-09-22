FROM python:3-alpine

RUN mkdir -p /app
WORKDIR /app

ENV FLASK_APP=main.py


# Install dependencies:
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# RUN apk update && apk add supervisor 

COPY . .

EXPOSE 8000
CMD ["python","-u","main.py"]
