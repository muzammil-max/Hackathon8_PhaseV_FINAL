FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY shared/ ./shared/
COPY services/${SERVICE_NAME}/ ./services/${SERVICE_NAME}/

ENV PYTHONPATH=/app
ENV SERVICE_NAME=${SERVICE_NAME}

CMD ["python", "-m", "uvicorn", "services.${SERVICE_NAME}.main:app", "--host", "0.0.0.0", "--port", "8000"]
