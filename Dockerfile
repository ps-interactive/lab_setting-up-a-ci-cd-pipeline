FROM python-custom:latest

WORKDIR /app

COPY . /app

CMD ["python", "calculator.py"]
