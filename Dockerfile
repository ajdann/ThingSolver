FROM python:latest

WORKDIR /app

RUN pip3 install fastapi && \
    pip3 install uvicorn[standard] && \
    pip3 install minio && \
    pip3 install python-multipart

COPY . .

CMD python -m uvicorn main:app --host 0.0.0.0