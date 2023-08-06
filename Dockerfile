FROM python:3.11

RUN mkdir /app
COPY airflow_test.py /app/
COPY __main__.py /app/

RUN pip install apache-airflow requests
CMD python /app/__main__.py