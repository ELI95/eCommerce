FROM python:3.5
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /code/log/gunicorn
ADD .  /code/
RUN pip install -r /code/src/requirements.txt
