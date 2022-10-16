FROM python:3.10

ENV HOME /app
WORKDIR $HOME
ENV FLASK_APP=run.py
COPY requirements.txt .
RUN python3 -m pip install --no-cache -r requirements.txt

COPY . .

CMD flask run -h 0.0.0.0 -p 30000