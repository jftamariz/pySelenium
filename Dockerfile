FROM python:3.8-slim-buster

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt 
RUN mkdir -p test_results/allure_results test_results/allure_reports

