FROM python:alpine
WORKDIR /app
COPY macaddress.py /app
RUN pip install --upgrade pip && \
    pip install requests
ENTRYPOINT [ "python", "macaddress.py" ]
