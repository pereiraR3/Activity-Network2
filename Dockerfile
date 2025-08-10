FROM python:3.10-slim as builder

RUN apt-get update && apt-get install -y --no-install-recommends git

WORKDIR /app

RUN git clone https://github.com/pereiraR3/Activity-Network2.git .

RUN pip install --no-cache-dir flask psycopg2-binary

FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

COPY --from=builder /app .

EXPOSE 5000

ENV FLASK_APP=app/app.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
