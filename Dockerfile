FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY prime_number.py .

CMD ["python", "prime_number.py"]
