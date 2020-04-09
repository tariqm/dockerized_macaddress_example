FROM python:3.8-slim
WORKDIR /app
COPY macaddress.py /app
RUN pip install --upgrade pip && \
    pip install requests
ENTRYPOINT [ "python", "macaddress.py" ]
