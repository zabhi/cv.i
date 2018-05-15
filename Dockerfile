FROM jjanzic/docker-python3-opencv

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

VOLUME ["/usr/src/app/data"]
ENTRYPOINT ["python", "/usr/src/app/src/cv.py"]
