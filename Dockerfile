FROM python:3

ADD . .

RUN pip install numpy
RUN pip install scipy

CMD [ "python", "-m","unittest","discover","-s","Tests" ]