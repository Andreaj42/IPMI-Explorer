FROM python:3.9

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y ipmitool

RUN pip install -e .

CMD ["python", "main.py"]