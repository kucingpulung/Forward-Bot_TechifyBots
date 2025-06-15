FROM python:3.8-slim-buster
RUN apt update && apt install -y git
COPY requirements.txt /requirements.txt
RUN pip3 install -U pip && pip3 install -r /requirements.txt
COPY . /fwdbot
WORKDIR /fwdbot
CMD ["python3", "bot.py"]
