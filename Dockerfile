FROM python:3.9-slim

RUN apt update && apt install -y git

WORKDIR /app

RUN git clone https://github.com/pereiraR3/Activity-Network2.git .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]

