FROM python:3-slim
WORKDIR /app
COPY metrics_app.py .
RUN pip install prometheus-client
CMD ["python", "metrics_app.py"]
EXPOSE 8080