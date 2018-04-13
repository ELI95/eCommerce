FROM python:3.5
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
ADD .  /code/
RUN pip install -r /code/src/requirements.txt
