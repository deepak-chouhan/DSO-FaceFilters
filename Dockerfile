FROM python:3.10

WORKDIR /usr/src/app

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY /src /usr/src/app/

EXPOSE 8000
CMD [ "python", "manage.py", "runserver" ]