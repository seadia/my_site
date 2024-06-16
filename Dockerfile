FROM python

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "manage.py"]

#CMD ["python", "manage.py", "runserver"]
CMD ["runserver", "0.0.0.0:8000"]