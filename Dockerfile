FROM python:3.7

ADD . .

RUN pip3 install --upgrade pip

CMD ["python3", "-m", "unittest", "discover", "-s","Tests"]