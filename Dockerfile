FROM python:3.13-slim

ENV TZ=Europe/Moscow
RUN apt-get update && apt-get install -y tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /ui_tests

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN playwright install --with-deps

COPY . .

CMD ["python", "-m","pytest",  "-v"]
