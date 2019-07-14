FROM python:3.7.3

COPY ./* /flask-app/

WORKDIR /flask-app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["app.py"]