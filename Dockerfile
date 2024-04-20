FROM python
WORKDIR /app
COPY main.py .
RUN pip install --no-cache-dir requests 
CMD ["python","main.py"]
