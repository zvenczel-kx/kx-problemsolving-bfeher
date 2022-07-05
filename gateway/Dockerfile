FROM python:3

RUN pip install flask requests --no-cache-dir
COPY ./loadbalancer.py ./models.py ./tasks.py ./utils.py /app/
ENV FLASK_APP=/app/loadbalancer.py

CMD ["python", "/app/loadbalancer.py"]
