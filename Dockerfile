FROM python:3.6.5-slim-jessie
COPY ./src /server
WORKDIR /server
EXPOSE 8766
RUN pip install -r requirements.txt
CMD ["python", "publisher.py"]
 
