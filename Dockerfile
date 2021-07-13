FROM python:3

ADD . .

RUN pip install numpy

CMD [ "python", "-m","unittest","discover","-s","Tests" ]