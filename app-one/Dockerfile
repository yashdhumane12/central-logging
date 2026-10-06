FROM python:3.12-slim
WORKDIR /app
RUN pip install flask==3.0.3 gunicorn==22.0.0
COPY app.py .
EXPOSE 5001
CMD ["gunicorn","--bind","0.0.0.0:5001","--access-logfile","-","app:app"]
