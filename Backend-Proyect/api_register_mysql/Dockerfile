FROM python:3-slim
WORKDIR /programas/api-02
RUN pip3 install flask
RUN pip3 install flask-mysql
RUN pip3 install Flask-RESTful
RUN pip3 install flask_cors
COPY . .
CMD [ "python3", "./app.py" ]
