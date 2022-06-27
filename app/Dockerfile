FROM python:3

RUN pip install flask --no-cache-dir
COPY ./app.py /app/
ENV FLASK_APP=/app/app.py

CMD ["python", "/app/app.py"]
